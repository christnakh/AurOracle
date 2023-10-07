
input_file = "kpdata.txt"
output_file = "kp-index.csv"
with open(input_file, 'r') as txt_file, open(output_file, 'w+') as csv_file:
    csv_file.write("Year, Day, Hour, Minute, Field Magnitude (nT), Vector Mag(NT), Bx (nT), By(nT), Bz(nT), Speed(km/s), Proton Density(n/cc), Temperature(k)\n")
    
    for line in txt_file:

        values = line.split()
        

        year = values[0]
        day = values[1]
        hour = values[2]
        minute = values[3]
        field_magnitude = values[4]
        vector_mag = values[5]
        bx_gse = values[6]
        by_gsm = values[7]
        bz_gsm = values[8]
        speed = values[9]
        proton_density = values[10]
        temperature = values[11]
        

        csv_file.write(f"{year},{day},{hour},{minute},{field_magnitude},{vector_mag},{bx_gse},{by_gsm},{bz_gsm},{speed},{proton_density},{temperature}\n")

print(f"Conversion complete. CSV file saved as {output_file}")
