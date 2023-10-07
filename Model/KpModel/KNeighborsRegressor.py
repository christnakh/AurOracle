import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn_reg = KNeighborsRegressor(n_neighbors=5) 
knn_reg.fit(X_scaled, y)

joblib.dump(knn_reg, 'trained_knn_regression_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
