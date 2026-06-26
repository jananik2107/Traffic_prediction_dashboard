import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
traffic_data = pd.read_csv("traffic_data/Traffic.csv")

# Encode target
label_encoder = LabelEncoder()
traffic_data["Traffic Situation"] = label_encoder.fit_transform(
    traffic_data["Traffic Situation"]
)

# Features and Target
X = traffic_data[["CarCount", "BikeCount", "BusCount", "TruckCount", "Total"]]
y = traffic_data["Traffic Situation"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

joblib.dump(model, "model/rf_model.pkl")
joblib.dump(X_test, "model/X_test.pkl")
joblib.dump(y_test, "model/y_test.pkl")

print("Model saved successfully!")