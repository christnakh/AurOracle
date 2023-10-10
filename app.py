from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import the CORS module
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.static_folder = 'static'  # Set the name of your "static" folder
app.static_url_path = '/static'  # Set the URL path for static files
CORS(app)  # Enable CORS for your app

# Load your machine learning models and scalers
model_kp = joblib.load('Model/KpModel/trained_random_forest_model.pkl')
scaler_kp = joblib.load('Model/KpModel/trained_standard_scaler.pkl')

model_data = joblib.load('Model/Data_Model/multioutput_regression_model.pkl')
scaler_data = joblib.load('Model/Data_Model/multiouput_standard_scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/predictkp', methods=['POST'])
def predict_kp():
    try:
        input_data = request.get_json()

        # Provide named features
        input_features = {f'feature{i}': float(
            input_data[f'feature{i}']) for i in range(1, 14)}

        # Use named features for scaling
        input_features_scaled = scaler_kp.transform(
            [list(input_features.values())])

        predicted_kp = model_kp.predict(input_features_scaled)[0]

        return jsonify({'predicted_kp': predicted_kp})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/predictdata', methods=['POST'])
def predict_data():
    try:
        kp_index = float(request.json['KpIndex'])

        kp_index_scaled = scaler_data.transform(np.array([[kp_index]]))

        predicted_features = model_data.predict(kp_index_scaled)

        response = {
            'Field Magnitude (nT)': predicted_features[0, 0],
            'Vector Mag(NT)': predicted_features[0, 1],
            'BX (nT)': predicted_features[0, 2],
            'BY(nT)': predicted_features[0, 3],
            'BZ(nT)': predicted_features[0, 4],
            'RMS SD B scalar (nT)': predicted_features[0, 5],
            'RMS SD field vector (nT)': predicted_features[0, 6],
            'RMS SD Bx (nT GSE)': predicted_features[0, 7],
            'RMS SD By (nT GSE)': predicted_features[0, 8],
            'RMS SD Bz (nT GSE)': predicted_features[0, 9],
            'Speed (km/s)': predicted_features[0, 10],
            'Proton Density (n/cc)': predicted_features[0, 11],
            'Temperature (K)': predicted_features[0, 12]
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
