import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
import joblib

data = pd.read_csv("../../dataset/solar_wind.csv")

X = data['Kp-Index'].values.reshape(-1, 1)
y = data.drop(columns=['Kp-Index'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

gb_regressor = GradientBoostingRegressor(n_estimators=100, random_state=42)

multioutput_regressor = MultiOutputRegressor(gb_regressor)

multioutput_regressor.fit(X_scaled, y)

joblib.dump(multioutput_regressor, 'multioutput_regression_model_gb.pkl')
joblib.dump(scaler, 'standard_scaler_gb.pkl')
