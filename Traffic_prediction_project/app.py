import streamlit as st

st.set_page_config(
    page_title="Traffic Prediction Dashboard",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Traffic Prediction Dashboard")

st.markdown("""
### Welcome!

This project predicts traffic congestion using Machine Learning.

### Available Pages:
- 🚗 Prediction
- 📊 Traffic Analysis
- 📅 24-Hour Forecast
- 📈 Model Performance

👈 Select a page from the left sidebar.
""")