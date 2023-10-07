import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('../dataset/solar_wind.csv')

target_fields = [
    'Field Magnitude (nT)', 'Vector Mag(NT)', 'BX (nT)', 'BY(nT)', 'BZ(nT)',
    'RMS SD B scalar (nT)', 'RMS SD field vector (nT)',
    'RMS SD Bx (nT GSE)', 'RMS SD By (nT GSE)', 'RMS SD Bz (nT GSE)',
    'Speed (km/s)', 'Proton Density (n/cc)', 'Temperature (K)', 'Kp-Index'
]

missing_fields = [field for field in target_fields if field not in data.columns]
if missing_fields:
    print(f"Missing target fields: {missing_fields}")
else:

    X = data.drop(target_fields, axis=1)

    if X.empty or not X.select_dtypes(include='number').any().any():
        print("No valid numeric data in X.")
    else:

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        y = data[target_fields]

        models = {
            'Linear Regression': LinearRegression(),
            'Ridge Regression': Ridge(),
            'Lasso Regression': Lasso(),
            'Decision Tree Regressor': DecisionTreeRegressor(),
            'Random Forest Regressor': RandomForestRegressor(),
            'Support Vector Regressor': SVR()
        }

        results = {'Model': [], 'MSE': [], 'R-squared': []}

        for target_field in target_fields:
            y_target = y[target_field]

            for model_name, model in models.items():
                model.fit(X_scaled, y_target)
                y_pred = model.predict(X_scaled)
                mse = mean_squared_error(y_target, y_pred)
                r2 = r2_score(y_target, y_pred)

                results['Model'].append(model_name)
                results['MSE'].append(mse)
                results['R-squared'].append(r2)

        results_df = pd.DataFrame(results)


        for target_field in target_fields:
            print(f"Results for {target_field}:")
            target_results = results_df[results_df.index % len(models) == 0] 
            target_results.index = range(len(models))  
            print(target_results)


            plt.figure(figsize=(12, 6))
            plt.bar(target_results['Model'], target_results['R-squared'], color='skyblue')
            plt.xlabel('Model')
            plt.ylabel('R-squared')
            plt.title(f'Model Comparison for {target_field} Prediction')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
