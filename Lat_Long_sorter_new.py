import csv


input_file_path = 'CSV_LAT LONG.csv'
output_file_path = 'output.csv'


min_latitude = 22.96
max_latitude = 23.01
min_longitude = 86.60
max_longitude = 86.67


def is_within_range(latitude, longitude):
    return min_latitude <= float(latitude) <= max_latitude and min_longitude <= float(longitude) <= max_longitude


with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:

    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)


    header = next(csv_reader)
    csv_writer.writerow(header)


    for row in csv_reader:
        latitude, longitude = row[0], row[1]
        if is_within_range(latitude, longitude):
            csv_writer.writerow(row)

print(f"Filtered data has been written to {output_file_path}")
