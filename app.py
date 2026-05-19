from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model
model = pickle.load(open("best_model.pkl", "rb"))

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Customer Churn Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    
    features = np.array([[
        data["Gender"],
        data["Senior Citizen"],
        data["Partner"],
        data["Dependents"],
        data["Tenure Months"],
        data["Phone Service"],
        data["Multiple Lines"],
        data["Internet Service"],
        data["Online Security"],
        data["Online Backup"],
        data["Device Protection"],
        data["Tech Support"],
        data["Streaming TV"],
        data["Streaming Movies"],
        data["Contract"],
        data["Paperless Billing"],
        data["Payment Method"],
        data["Monthly Charges"],
        data["Total Charges"],
        data["CLTV"]
    ]])
    
    prediction = model.predict(features)
    
    result = int(prediction[0])
    
    if result == 1:
        output = "Customer Will Churn"
    else:
        output = "Customer Will Stay"
        
    return jsonify({
        "Prediction": output
    })
    
if __name__ == "__main__":
    app.run(debug=True)