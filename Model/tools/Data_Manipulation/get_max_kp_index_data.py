import pandas as pd

def get_max_kp_index_data(csv_file):   
    df = pd.read_csv(csv_file)
    max_kp_row = df[df['Kp-Index'] >= 7.0]
    max_kp_data = max_kp_row[['Year', 'Day', 'Hour', 'Field Magnitude (nT)', 'Vector Mag(NT)',
                              'BX (nT)', 'BY(nT)', 'BZ(nT)', 'RMS SD B scalar (nT)',
                              'RMS SD field vector (nT)', 'RMS SD Bx (nT GSE)',
                              'RMS SD By (nT GSE)', 'RMS SD Bz (nT GSE)', 'Speed (km/s)',
                              'Proton Density (n/cc)', 'Temperature (K)', 'Kp-Index']]

    return max_kp_data

csv_file = 'solar_wind_cleaned.csv' 
max_kp_data = get_max_kp_index_data(csv_file)
print(max_kp_data)
