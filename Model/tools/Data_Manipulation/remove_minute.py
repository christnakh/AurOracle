import pandas as pd

def remove_minute_from_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    df = df.drop(df.columns[3], axis=1)

    df.to_csv(output_file, index=False)

input_file = 'all.csv'
output_file = 'solar_wind_without_minute.csv'

remove_minute_from_csv(input_file, output_file)
