import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import StandardScaler
import joblib

data = pd.read_csv("../dataset/solar_wind.csv")

# Separate features (X) and target variables (Kp-Index and other features)
X = data['Kp-Index'].values.reshape(-1, 1)
y = data.drop(columns=['Kp-Index'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

multioutput_regressor = MultiOutputRegressor(rf_regressor)

multioutput_regressor.fit(X_scaled, y)

joblib.dump(multioutput_regressor,
            'multioutput_regression_model.pkl')
joblib.dump(scaler, 'multiouput_standard_scaler.pkl')
