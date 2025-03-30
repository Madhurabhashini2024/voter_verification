# Aadhaar-Based Biometric Verification with AI-Powered Anomaly Detection

## Overview

This project aims to enhance the security and efficiency of the voter verification process by using Aadhaar-based biometric authentication and AI-powered anomaly detection. The system is designed to reduce fraud, speed up verification, and improve the overall voting experience.

**Disclaimer:** This is a simplified prototype and is *not* intended for production use without thorough security review and testing. It uses simulated data and simplified authentication mechanisms for demonstration purposes.

## Features

*   **Aadhaar-Based Verification:** Simulates verifying voter identity using Aadhaar numbers.
*   **Biometric Authentication:**  Placeholder for integrating with a fingerprint scanner for biometric verification (requires scanner SDK).
*   **AI-Powered Anomaly Detection:** Uses a machine learning model to detect potential anomalies in voter data.
*   **Simplified Authentication:** Implements a basic token-based authentication system (JWT) for demonstration.
*   **Flask Web Application:** Provides a user-friendly web interface for voter verification.

## Table of Contents

- [Aadhaar-Based Biometric Verification with AI-Powered Anomaly Detection](#aadhaar-based-biometric-verification-with-ai-powered-anomaly-detection)
  - [Overview](#overview)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Training the Anomaly Detection Model](#training-the-anomaly-detection-model)
    - [Running the Flask Application](#running-the-flask-application)
    - [Using the Web Interface](#using-the-web-interface)
  - [Security Considerations](#security-considerations)
  - [Limitations](#limitations)
  - [Future Work](#future-work)
  - [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.7+:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **Pip:** (Usually comes with Python)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd voter_verification
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Set the `SECRET_KEY` environment variable:**

    *   This is crucial for security.  Choose a strong, random string and set it as an environment variable.
    *   **Linux/macOS:**

        ```bash
        export SECRET_KEY="YourStrongSecretKey"
        ```

    *   **Windows:**

        ```bash
        set SECRET_KEY="YourStrongSecretKey"
        ```

    *   **Note:** You can also set environment variables in your deployment environment (e.g., Heroku, AWS).

## Usage

### Training the Anomaly Detection Model

1.  Run the `train_model.py` script to train the anomaly detection model:

    ```bash
    python train_model.py
    ```

    This will generate the `anomaly_detection_model.pkl` file, which is used by the Flask application.  This step only needs to be done once, or when you want to update the model.

### Running the Flask Application

1.  Make sure the `SECRET_KEY` environment variable is set.
2.  Run the `app.py` script:

    ```bash
    python app.py
    ```

    This will start the Flask development server.  You should see output indicating the server is running, and it will likely provide an address like `http://127.0.0.1:5000/`.

### Using the Web Interface

1.  **Open your web browser:**  Navigate to the address provided when you ran `app.py` (e.g., `http://127.0.0.1:5000/`). You should see the Voter Verification page.

2.  **Login to Obtain a Token:**

    *   You'll first see a "Login" form.
    *   Enter the **username** `admin` and the **password** `password`.  **IMPORTANT:  These are placeholder credentials and should be changed in a real system.**
    *   Click the "Get Token" button.
    *   If the login is successful, you'll see an alert saying "Login Successful! Token saved."  The login form will disappear, and the Voter Verification form will appear.  The token is now stored in your browser's memory for this session.

3.  **Verify a Voter:**

    *   In the "Verify Voter" form, enter a 12-digit Aadhaar number in the "Aadhaar Number" field.
    *   Click the "Verify" button.

4.  **View the Results:**

    *   The results of the verification will be displayed below the form.
    *   **Success:** If the Aadhaar number is found in the simulated database and the (simulated) fingerprint matches, you'll see the voter's name and the anomaly status.
        *   **Anomaly Status:**
            *   "Anomaly Detected": The AI model has identified potential issues with this voter's data based on the simulated anomaly detection features (age, gender, voting frequency).  This *does not* necessarily mean the voter is fraudulent, but it flags the case for further review.
            *   "No Anomaly": The AI model has not detected any anomalies.
    *   **Error:** If the Aadhaar number is not found or the fingerprint doesn't match, an error message will be displayed.

5.  **Example Aadhaar Numbers (for testing):**

    *   Use these Aadhaar numbers for testing (they are in the simulated database):
        *   `123456789012` (Alice Smith - No Anomaly)
        *   `987654321098` (Bob Johnson - No Anomaly)

    *   The anomaly detection is based on the simulated data in `train_model.py`.  The model is very simple, so the results are for demonstration only.

6.  **Understanding the Workflow:**

    *   The system simulates the process of:
        1.  A voter presenting their Aadhaar number at a polling booth.
        2.  The system verifying their identity against the Aadhaar database (simulated).
        3.  The system using a fingerprint scanner (simulated) to confirm their identity.
        4.  The system running the voter's data through an AI model to detect potential anomalies that might indicate fraud.
        5.  Election officials reviewing any flagged cases to make a final determination.

## Security Considerations

**WARNING: This project is not secure enough for production use without significant modifications.**

*   **Authentication:** The provided token-based authentication is a simplified example.  Use a robust authentication system like OAuth 2.0 or JWT with proper user management in a real application.
*   **Secret Key:** The `SECRET_KEY` must be stored securely and never committed to version control. Use environment variables or secure configuration files.
*   **Input Sanitization:** The project includes basic input sanitization, but more comprehensive measures are needed to prevent injection attacks.
*   **HTTPS:**  Always use HTTPS to encrypt communication between the client and the server.
*   **Data Security:**  Handle sensitive data (e.g., Aadhaar numbers, fingerprint data) with extreme care.  Use proper encryption and access control mechanisms.  Avoid storing this data if possible.
*   **Dependencies:** Regularly update dependencies to patch security vulnerabilities.

## Limitations

*   **Simulated Data:** Uses simulated Aadhaar data and fingerprint data.
*   **Simplified Authentication:** Implements a basic authentication system for demonstration purposes.
*   **No Real Fingerprint Scanner Integration:** Requires integration with a real fingerprint scanner and associated SDK.
*   **Limited Error Handling:** Error handling is basic and needs to be improved.
*   **Scalability:** The application is not designed for high traffic or large-scale deployments.
*   **Security:** The system has not undergone a thorough security audit and may contain vulnerabilities.
*   **Anomaly Detection Model:** The anomaly detection model is trained on a small, synthetic dataset and may not generalize well to real-world data.

## Future Work

*   **Integrate with a real fingerprint scanner.**
*   **Implement a more robust authentication system.**
*   **Improve input sanitization and validation.**
*   **Enhance error handling and logging.**
*   **Develop a more sophisticated anomaly detection model using real-world data.**
*   **Implement a secure and scalable database.**
*   **Deploy the application to a production environment with HTTPS enabled.**
*   **Conduct a thorough security audit.**
*   **Implement proper data encryption and access control mechanisms.**
*   **Develop a user-friendly admin interface for managing users and data.**
*   **Add support for other biometric authentication methods.**

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

