import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor 
import joblib

data = pd.read_csv("dataset/solar_wind.csv")

X = data.drop(columns=['Kp-Index'])
y = data['Kp-Index']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

decision_tree_reg = DecisionTreeRegressor(max_depth=5) 
decision_tree_reg.fit(X_scaled, y)

joblib.dump(decision_tree_reg, 'trained_decision_tree_regression_model.pkl')
joblib.dump(scaler, 'trained_standard_scaler.pkl')
