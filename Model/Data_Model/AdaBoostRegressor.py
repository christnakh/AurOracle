import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("../../dataset/solar_wind.csv")

X = data['Kp-Index'].values.reshape(-1, 1)
y = data.drop(columns=['Kp-Index'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

adaboost_regressor = AdaBoostRegressor(
    base_estimator=DecisionTreeRegressor(max_depth=5), 
    n_estimators=50,
    random_state=42
)

multioutput_regressor = MultiOutputRegressor(adaboost_regressor)

multioutput_regressor.fit(X_scaled, y)

joblib.dump(multioutput_regressor, 'multioutput_regression_model_adaboost.pkl')
joblib.dump(scaler, 'standard_scaler_adaboost.pkl')
