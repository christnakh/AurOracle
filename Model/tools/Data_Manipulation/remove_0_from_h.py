import csv

def transform_data(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  
        transformed_data = []

        for row in reader:
            year, day_of_year, hour, kp_index = row
            day_of_year = str(int(day_of_year)) 
            hour = int(float(hour)) 
            transformed_data.append([year, day_of_year, hour, kp_index])

    with open(output_csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Year', 'DayOfYear', 'Hour', 'Kp-Index'])
        writer.writerows(transformed_data)

input_csv_file = 'output.csv'
output_csv_file = 'output.csv'
transform_data(input_csv_file, output_csv_file)
