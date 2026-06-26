import streamlit as st
from datetime import datetime

st.title("🚦 Smart Traffic Prediction")

now = datetime.now()

st.write("### Current Information")
st.write("📅 Date:", now.strftime("%d-%m-%Y"))
st.write("⏰ Time:", now.strftime("%H:%M:%S"))
st.write("📆 Day:", now.strftime("%A"))

weather = st.selectbox(
    "Select Weather",
    ["Clear", "Cloudy", "Rainy", "Snowy"]
)

if st.button("Predict"):

    if weather == "Clear":
        traffic = "Low"
        delay = "2 Minutes"

    elif weather == "Cloudy":
        traffic = "Normal"
        delay = "5 Minutes"

    elif weather == "Rainy":
        traffic = "High"
        delay = "15 Minutes"

    else:
        traffic = "Heavy"
        delay = "30 Minutes"

    st.success(f"Traffic Level : {traffic}")
    st.info(f"Estimated Delay : {delay}")