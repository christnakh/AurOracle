import pandas as pd
from datetime import datetime, timedelta

def replace_day_with_month(input_file, output_file):
    df = pd.read_csv(input_file)

    day_column_name = 'Day'

    df[day_column_name] = df[day_column_name].astype(int)

    df['Date'] = df.apply(lambda row: datetime(row['Year'], 1, 1) + timedelta(days=row[day_column_name] - 1), axis=1)

    df['Month'] = df['Date'].dt.strftime('%B')

    df = df.drop(columns=[day_column_name])

    df = df[['Year', 'Month', 'Hour', 'Minute', 'Field Magnitude (nT)', 'Vector Mag(NT)', 'Bx (nT)', 'By(nT)', 'Bz(nT)', 'Speed(km/s)', 'Proton Density(n/cc)', 'Temperature(k)']]

    df.to_csv(output_file, index=False)
input_file = 'solar_wind_without_minute.csv'
output_file = 'your_output_file.csv'
replace_day_with_month(input_file, output_file)
