import pandas as pd

def remove_and_save_columns(input_file, output_file):
    df = pd.read_csv(input_file)

    columns_to_remove = ["Field Magnitude (nT)","Vector Mag(NT)","BX (nT)","BY(nT)","BZ(nT)","RMS SD B scalar (nT)","RMS SD field vector (nT)","RMS SD Bx (nT GSE)","RMS SD By (nT GSE)","RMS SD Bz (nT GSE)"]

    columns_to_remove = [col for col in columns_to_remove if col in df.columns]

    df = df.drop(columns=columns_to_remove, axis=1)

    df.to_csv(output_file, index=False)
    
input_file = 'solar_wind.csv'
output_file = 'kp_data.csv'
remove_and_save_columns(input_file, output_file)
