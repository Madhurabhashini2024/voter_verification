import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib  # For saving and loading the model

# Simulated Aadhaar database (replace with a real database)
aadhaar_data = {
    "123456789012": {
        "name": "Alice Smith",
        "dob": "1990-05-15",
        "address": "123 Main St, Anytown",
        "fingerprint_hash": "e5b7a2c8d9f0b3a1c2e3f4a5b6c7d8e9"  # Example hash
    },
    "987654321098": {
        "name": "Bob Johnson",
        "dob": "1985-10-20",
        "address": "456 Oak Ave, Anytown",
        "fingerprint_hash": "f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6"  # Example hash
    }
}

def verify_aadhaar(aadhaar_number, fingerprint_hash):
    """Simulates Aadhaar verification."""
    if aadhaar_number in aadhaar_data:
        if aadhaar_data[aadhaar_number]["fingerprint_hash"] == fingerprint_hash:
            return {
                "status": "success",
                "name": aadhaar_data[aadhaar_number]["name"],
                "dob": aadhaar_data[aadhaar_number]["dob"],
                "address": aadhaar_data[aadhaar_number]["address"]
            }
        else:
            return {"status": "error", "message": "Fingerprint mismatch"}
    else:
        return {"status": "error", "message": "Aadhaar number not found"}

# Load the trained anomaly detection model (assuming it's already trained)
try:
    model = joblib.load('anomaly_detection_model.pkl')
except FileNotFoundError:
    print("Anomaly detection model not found.  Please train the model first.")
    model = None # Or create a default/placeholder model

def detect_anomaly(age, gender, voting_frequency, voter_id_valid):
    """Detects anomalies based on voter data."""
    if model is None:
        return "Model not loaded"  # Handle the case where the model is not available

    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'voting_frequency': [voting_frequency],
        'voter_id_valid': [voter_id_valid]
    })

    # Make a prediction
    prediction = model.predict(input_data)[0]  # Access the first element
    return int(prediction) # Ensure it's an integer (0 or 1)
