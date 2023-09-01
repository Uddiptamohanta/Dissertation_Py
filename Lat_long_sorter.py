import csv


def sort_coordinates_in_range(csv_file, min_lat, max_lat, min_lon, max_lon):
    coordinates = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) >= 2:
                lat = float(row[0])
                lon = float(row[1])
                if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
                    coordinates.append((lat, lon))

    sorted_coordinates = sorted(coordinates)
    return sorted_coordinates


if __name__ == "__main__":
    csv_file = "CSV_LAT LONG.csv"  # Replace with your CSV file name
    min_lat = 22.96  # Replace with the minimum latitude of the range
    max_lat = 23.01  # Replace with the maximum latitude of the range
    min_lon = 86.60  # Replace with the minimum longitude of the range
    max_lon = 86.67  # Replace with the maximum longitude of the range

    sorted_coordinates = sort_coordinates_in_range(csv_file, min_lat, max_lat, min_lon, max_lon)

    print("Sorted coordinates within the range:")
    for lat, lon in sorted_coordinates:
        print(f"Latitude: {lat}, Longitude: {lon}")
