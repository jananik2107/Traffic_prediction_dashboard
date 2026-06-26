import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

st.title("🤖 Model Performance")

# Load model and test data
model = joblib.load("model/rf_model.pkl")
X_test = joblib.load("model/X_test.pkl")
y_test = joblib.load("model/y_test.pkl")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

st.subheader("Model Accuracy")
st.metric("Accuracy", f"{accuracy*100:.2f}%")

# Confusion Matrix
st.subheader("Confusion Matrix")

fig, ax = plt.subplots(figsize=(6,5))
cm = confusion_matrix(y_test, y_pred)

labels = ["Heavy", "High", "Low", "Normal"]

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=labels
)

disp.plot(ax=ax, cmap="Blues")

st.pyplot(fig)

# Classification Report
st.subheader("Classification Report")

report = classification_report(
    y_test,
    y_pred,
    target_names=["Heavy", "High", "Low", "Normal"],
    output_dict=True
)
report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df, use_container_width=True)

# Feature Importance
st.subheader("Feature Importance")

features = [
    "CarCount",
    "BikeCount",
    "BusCount",
    "TruckCount",
    "Total"
]

importance = model.feature_importances_

fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.bar(features, importance)
ax2.set_ylabel("Importance")
ax2.set_title("Feature Importance")

st.pyplot(fig2)