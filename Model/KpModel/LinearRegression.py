import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

linear_reg = LinearRegression()
linear_reg.fit(X_scaled, y)

joblib.dump(linear_reg, 'trained_linear_regression_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
