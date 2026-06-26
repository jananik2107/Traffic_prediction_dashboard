import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📅 24-Hour Traffic Forecast")

# Legend
st.subheader("Traffic Level Guide")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("🟢 Low")

with col2:
    st.warning("🟡 Normal")

with col3:
    st.warning("🟠 High")

with col4:
    st.error("🔴 Heavy")

st.markdown("---")

# Load Dataset
df = pd.read_csv("traffic_data/Traffic.csv")

# Convert Time to Hour
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

# Average traffic for each hour
forecast = df.groupby("Hour")["Total"].mean().reset_index()

# Traffic Level
def level(x):
    if x < 60:
        return "Low"
    elif x < 100:
        return "Normal"
    elif x < 140:
        return "High"
    else:
        return "Heavy"

forecast["Traffic"] = forecast["Total"].apply(level)

# Assign Colors
colors = []

for traffic in forecast["Traffic"]:
    if traffic == "Low":
        colors.append("green")
    elif traffic == "Normal":
        colors.append("yellow")
    elif traffic == "High":
        colors.append("orange")
    else:
        colors.append("red")

st.subheader("Today's 24-Hour Traffic Timeline")

# Timeline Graph
fig, ax = plt.subplots(figsize=(14, 2.5))

ax.barh(
    y=["Traffic"],
    width=[1] * len(forecast),
    left=forecast["Hour"],
    color=colors,
    edgecolor="black",
    height=0.5
)

ax.set_xlim(0, 24)
ax.set_xticks(range(24))
ax.set_yticks([])
ax.set_xlabel("Hour of Day")
ax.set_title("Traffic Congestion Timeline")

st.pyplot(fig)

# Peak Traffic Information
peak = forecast.loc[forecast["Total"].idxmax()]

st.subheader("Peak Traffic Information")

st.success(f"🚗 Peak Traffic Hour : {int(peak['Hour'])}:00")

st.info(f"📊 Average Vehicle Count : {peak['Total']:.0f}")

# Hourly Forecast Table
st.subheader("Hourly Forecast")

forecast_table = forecast[["Hour", "Traffic"]].rename(
    columns={
        "Hour": "Hour",
        "Traffic": "Traffic Level"
    }
)

st.dataframe(forecast_table, use_container_width=True)
