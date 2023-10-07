import pandas as pd

input_file_path = 'final_data.csv'
data = pd.read_csv(input_file_path)


def round_kp_index(kp_index):
    return round(kp_index)

data['Kp-Index'] = data['Kp-Index'].apply(round_kp_index)

output_file_path = 'output.csv'

data.to_csv(output_file_path, index=False)

print(f'Data with rounded Kp-Index values saved to {output_file_path}')
