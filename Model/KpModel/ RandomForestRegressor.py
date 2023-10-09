import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv("../dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

best_random_forest = RandomForestRegressor(
    n_estimators=100, max_depth=None, min_samples_split=2, random_state=42)
best_random_forest.fit(X_scaled, y)

joblib.dump(best_random_forest, 'trained_random_forest_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
