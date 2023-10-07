import pandas as pd
from datetime import datetime

def process_date(df):
    df['Year'] = df['Year'].astype(float)
    df['Month'] = df['Month'].astype(float)
    df['Day'] = df['Day'].astype(float)
    df['Hour'] = pd.to_numeric(df['Hour'], errors='coerce').fillna(0).astype(int)
    df['Date'] = df.apply(lambda row: datetime(row['Year'], 1, row['Day'], row['Hour'], 0), axis=1)
    df['DayOfYear'] = df['Date'].dt.dayofyear

    return df


input_file = 'kp-index.csv' 
output_file = 'your_output_file.csv' 
df = pd.read_csv(input_file)

df_processed = process_date(df)

df_processed.to_csv(output_file, index=False)
