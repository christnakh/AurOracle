import csv

def extract_and_save_data(input_txt_file, output_csv_file):
    extracted_data = []

    with open(input_txt_file, 'r') as txtfile:
        for line in txtfile:
    
            fields = line.strip().split()
    
            if len(fields) >= 8:
        
                extracted_row = [fields[i] for i in [0, 1, 2, 3, 7]]
                extracted_data.append(extracted_row)

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(['Column0', 'Column1', 'Column2', 'Column3', 'Column7'])

        csv_writer.writerows(extracted_data)
input_txt_file = 'kpdata.txt'
output_csv_file = 'kp-index.csv'
extract_and_save_data(input_txt_file, output_csv_file)
