import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

best_gradient_boosting = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
best_gradient_boosting.fit(X_scaled, y)

joblib.dump(best_gradient_boosting, 'trained_gradient_boosting_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
