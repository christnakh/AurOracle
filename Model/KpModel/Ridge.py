import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

ridge_reg = Ridge(alpha=1.0) 
ridge_reg.fit(X_scaled, y)

joblib.dump(ridge_reg, 'trained_ridge_regression_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
