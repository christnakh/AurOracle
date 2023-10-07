import csv

def format_data(input_file, output_file):
    formatted_lines = []

    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        next(reader)
    
        for row in reader:
            year, day, hour, field_magnitude, vector_mag, bx, by, bz, rms_sd_scalar, rms_sd_vector, rms_sd_bx, rms_sd_by, rms_sd_bz, speed, proton_density, temperature, kp_index = row

            formatted_kp_index = "{:.1f}".format(float(kp_index))

            formatted_line = [year, day, hour, field_magnitude, vector_mag, bx, by, bz, rms_sd_scalar, rms_sd_vector, rms_sd_bx, rms_sd_by, rms_sd_bz, speed, proton_density, temperature, formatted_kp_index]
            formatted_lines.append(formatted_line)

        writer.writerow(['Year', 'Day', 'Hour', 'Field Magnitude (nT)', 'Vector Mag(NT)', 'BX (nT)', 'BY(nT)', 'BZ(nT)', 'RMS SD B scalar (nT)', 'RMS SD field vector (nT)', 'RMS SD Bx (nT GSE)', 'RMS SD By (nT GSE)', 'RMS SD Bz (nT GSE)', 'Speed (km/s)', 'Proton Density (n/cc)', 'Temperature (K)', 'Kp-Index'])
        writer.writerows(formatted_lines)

input_file = 'final_data.csv'
output_file = 'output_data.csv'
format_data(input_file, output_file)
print(f"Formatted data written to {output_file}")
