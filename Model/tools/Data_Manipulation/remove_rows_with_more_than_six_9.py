import csv

def remove_rows_with_more_than_six_9(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  
        data_to_keep = []

        for row in reader:
            if all(value.count('9') <= 6 for value in row):
                data_to_keep.append(row)

    with open(output_csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data_to_keep)

input_csv_file = 'final_data.csv'
output_csv_file = 'output.csv'
remove_rows_with_more_than_six_9(input_csv_file, output_csv_file)
