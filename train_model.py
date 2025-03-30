
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Data Preparation (Simulated Data)
data = {
    'age': [30, 45, 60, 25, 35, 50, 70, 28, 40, 55, 30, 45, 60, 25, 35],
    'gender': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # 0 = Male, 1 = Female
    'voting_frequency': [5, 10, 12, 3, 7, 15, 18, 4, 9, 11, 5, 10, 12, 3, 7],
    'voter_id_valid': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'anomaly': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# 2. Feature Selection
X = df[['age', 'gender', 'voting_frequency', 'voter_id_valid']]
y = df['anomaly']

# 3. Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'anomaly_detection_model.pkl')
print("Anomaly detection model trained and saved as anomaly_detection_model.pkl")

