# Customer Churn Prediction System

Machine Learning-based Customer Churn Prediction System with Flask API deployment using Logistic Regression, Random Forest, and XGBoost.

---

# Project Overview

This project aims to predict whether a customer will churn or stay using Machine Learning classification models.  

The project includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Classification Modeling
- Model Comparison
- Model Deployment using Flask API

---

# Dataset

Dataset used:

- IBM Telco Customer Churn Dataset

Target variable:

- `Churn Label`

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Flask
- Pickle

---

# Machine Learning Models

The following classification models were used:

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

---

# Model Results

| Model | Accuracy | F1 Score |
|------|------|------|
| Logistic Regression | 0.802 | 0.622 |
| Random Forest | 0.799 | 0.603 |
| XGBoost | 0.798 | 0.610 |

Best Model:

- Logistic Regression

---

# Features Used

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure Months
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- CLTV

---

# Data Preprocessing

Steps performed:

- Missing value handling
- Data cleaning
- Label Encoding
- Feature selection
- Data leakage removal
- Train-test split

---

# API Deployment

The trained model was deployed using Flask API.

## Run Flask API

```bash
python app.py
API Endpoint
POST /predict

Example URL:

http://127.0.0.1:5000/predict
Example Request
{
    "Gender": 1,
    "Senior Citizen": 0,
    "Partner": 1,
    "Dependents": 0,
    "Tenure Months": 12,
    "Phone Service": 1,
    "Multiple Lines": 0,
    "Internet Service": 1,
    "Online Security": 1,
    "Online Backup": 0,
    "Device Protection": 1,
    "Tech Support": 0,
    "Streaming TV": 1,
    "Streaming Movies": 1,
    "Contract": 0,
    "Paperless Billing": 1,
    "Payment Method": 2,
    "Monthly Charges": 75.5,
    "Total Charges": 1200.5,
    "CLTV": 3500
}

---

Example Response
{
    "Prediction": "Customer Will Churn"
}

---

Installation
Clone repository:
git clone https://github.com/your-username/customer-churn-prediction-system.git

Install dependencies:
pip install -r requirements.txt

---

Run API:
python app.py

---

Project Structure
customer-churn-prediction-system/
│
├── dataset/
├── notebooks/
├── app.py
├── best_model.pkl
├── requirements.txt
└── README.md

---

Future Improvements

- Deploy to Render/Heroku
- Build frontend interface
- Hyperparameter tuning
- Add Docker support

Author
Muhammad Tamami