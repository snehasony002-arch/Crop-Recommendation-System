import joblib

# Load the trained model
model = joblib.load("models/crop_model.pkl")

print("🌱 Crop Recommendation System")
print("-" * 30)

N = float(input("Enter Nitrogen (N): "))
P = float(input("Enter Phosphorus (P): "))
K = float(input("Enter Potassium (K): "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter pH: "))
rainfall = float(input("Enter Rainfall: "))

# Store input values in a list
data = [[N, P, K, temperature, humidity, ph, rainfall]]

# Predict the crop
prediction = model.predict(data)

print("\n✅ Recommended Crop:", prediction[0])