import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

best_svr = SVR(kernel='linear', C=1.0)
best_svr.fit(X_scaled, y)

joblib.dump(best_svr, 'trained_svm_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
