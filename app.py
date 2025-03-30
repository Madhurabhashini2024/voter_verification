import os
from flask import Flask, render_template, request, jsonify, abort
from functools import wraps
import jwt  # For simplified JWT
import datetime
import hashlib # For input sanitization
import utils  # Helper functions in utils.py

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'YourFallbackSecretKey'  # Get from environment
if not app.config['SECRET_KEY']:
    print("WARNING: No SECRET_KEY found in environment. Using fallback.  This is INSECURE in production.")

# Simplified JWT-based Authentication
def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expires in 30 minutes
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # You could check user roles/permissions here based on data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not (auth.username == 'admin' and auth.password == 'password'): # REPLACE WITH SECURE CREDENTIALS
        return jsonify({'message': 'Authentication required'}), 401

    token = generate_token(auth.username)
    return jsonify({'token': token})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
@requires_auth  # Protect the registration endpoint
def register():
    # In a real system, you'd create an admin interface
    # to manage user registration.  This is just a placeholder.
    return jsonify({'message': 'Registration endpoint (requires authentication)'})

@app.route('/verify', methods=['POST'])
def verify():
    try:
        aadhaar_number = request.form['aadhaar_number']

        # Input Sanitization (hashing for basic protection)
        hashed_aadhaar = hashlib.sha256(aadhaar_number.encode()).hexdigest()

        # Basic input validation
        if not (aadhaar_number and aadhaar_number.isdigit() and len(aadhaar_number) == 12):
            return jsonify({'status': 'error', 'message': 'Invalid Aadhaar number'}), 400

        # Simulate fingerprint capture (replace with actual scanner)
        fingerprint_hash = "e5b7a2c8d9f0b3a1c2e3f4a5b6c7d8e9"  # Simulate it

        # Aadhaar Verification
        verification_result = utils.verify_aadhaar(aadhaar_number, fingerprint_hash)

        if verification_result['status'] == 'success':
            # Anomaly Detection
            age = 30  # Replace with actual age from verification_result
            gender = 0  # Replace with actual gender
            voting_frequency = 5  # Replace with actual voting frequency

            anomaly_status = utils.detect_anomaly(age, gender, voting_frequency, 1)

            # Prepare the response
            response = {
                'status': 'success',
                'name': verification_result['name'],
                'anomaly': anomaly_status
            }
            return jsonify(response)
        else:
            return jsonify({'status': 'error', 'message': verification_result['message']}), 400
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
