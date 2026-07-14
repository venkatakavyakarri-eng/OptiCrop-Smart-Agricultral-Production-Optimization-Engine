import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ===========================
# Load Dataset
# ===========================

data = pd.read_csv("dataset/Crop_Recommendation.csv")

print("====================================")
print("Dataset Loaded Successfully")
print("====================================")

print("Dataset Shape :", data.shape)

print("\nFirst 5 Rows:")
print(data.head())

print("\nCrop Categories:")
print(data["label"].unique())

print("\nCrop Count:")
print(data["label"].value_counts())

# ===========================
# Features and Target
# ===========================

X = data[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]]

y = data["label"]

# ===========================
# Encode Labels
# ===========================

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("\nEncoded Classes:")
print(label_encoder.classes_)

# ===========================
# Train Test Split
# ===========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

# ===========================
# Train Model
# ===========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ===========================
# Test Accuracy
# ===========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n====================================")
print(f"Model Accuracy : {accuracy*100:.2f}%")
print("====================================")

# ===========================
# Save Model
# ===========================

joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("\nModel saved successfully.")
print("Label Encoder saved successfully.")

# ===========================
# Test Prediction
# ===========================

sample = pd.DataFrame([{
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.879744,
    "humidity": 82.002744,
    "ph": 6.502985,
    "rainfall": 202.935536
}])

prediction = model.predict(sample)

crop = label_encoder.inverse_transform(prediction)

print("\nSample Prediction :", crop[0])