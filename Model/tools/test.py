import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv('dataset/solar_wind.csv')

X = data[['Field Magnitude (nT)', 'Vector Mag(NT)', 'BX (nT)', 'BY(nT)', 'BZ(nT)',
          'RMS SD B scalar (nT)', 'RMS SD field vector (nT)', 'RMS SD Bx (nT GSE)',
          'RMS SD By (nT GSE)', 'RMS SD Bz (nT GSE)', 'Speed (km/s)',
          'Proton Density (n/cc)', 'Temperature (K)']]
y = data['Kp-Index']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

results = {}

algorithms = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(),
    'Random Forest Regressor': RandomForestRegressor(),
    'Support Vector Regressor': SVR()
}

for name, model in algorithms.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'MAE': mae, 'MSE': mse, 'R2 Score': r2}

for name, metrics in results.items():
    print(f'{name}:')
    print(f'Mean Absolute Error (MAE): {metrics["MAE"]:.2f}')
    print(f'Mean Squared Error (MSE): {metrics["MSE"]:.2f}')
    print(f'R-squared (R2) Score: {metrics["R2 Score"]:.2f}')
    print()

best_algorithm = min(results, key=lambda x: results[x]['MAE'])
print(f'Best Algorithm: {best_algorithm}')
