import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Traffic Data Analysis")

# Load data
df = pd.read_csv("traffic_data/Traffic.csv")

# ---------------- Graph 1 ----------------
st.subheader("1. Average Vehicle Count")

vehicle_avg = df[['CarCount','BikeCount','BusCount','TruckCount']].mean()

fig, ax = plt.subplots()
vehicle_avg.plot(kind='bar', ax=ax)
plt.ylabel("Average Count")
st.pyplot(fig)

# ---------------- Graph 2 ----------------
st.subheader("2. Traffic Situation Distribution")

traffic = df['Traffic Situation'].value_counts()

fig, ax = plt.subplots()
traffic.plot(kind='pie', autopct='%1.1f%%', ax=ax)
plt.ylabel("")
st.pyplot(fig)

# ---------------- Graph 3 ----------------
st.subheader("3. Hourly Traffic Volume")

# Extract only the hour
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

hourly = df.groupby("Hour")["Total"].mean()

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(hourly.index, hourly.values, marker='o')
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Average Traffic Volume")
ax.set_xticks(range(24))
st.pyplot(fig)

# ---------------- Graph 4 ----------------
st.subheader("4. Total Vehicle Count Distribution")

fig, ax = plt.subplots()
df["Total"].hist(bins=20, ax=ax)
ax.set_xlabel("Total Vehicles")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.subheader("5. Congestion Heatmap")

if "Time" in df.columns and "Day of the week" in df.columns and "Total" in df.columns:

    df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

    heatmap_data = df.pivot_table(
        values="Total",
        index="Day of the week",
        columns="Hour",
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(10,4))
    sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt=".0f", ax=ax)

    ax.set_title("Traffic Congestion Heatmap")
    st.pyplot(fig)

else:
    st.warning("Required columns not found.")