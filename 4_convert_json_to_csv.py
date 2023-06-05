import requests
import json
import csv

def download_and_convert_to_csv():
    # Step 1: Download the data
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the data: {e}")
        return

    # Step 2: Process the data and convert it to the proper structure
    processed_data = []
    for entry in data:
        if "geolocation" in entry and "coordinates" in entry["geolocation"]:
            coordinates = entry["geolocation"]["coordinates"]
        else:
            coordinates = []
        processed_entry = {
            "Name of Earth Meteorite": entry.get("name", ""),
            "id": entry.get("id", ""),
            "nametype": entry.get("nametype", ""),
            "recclass": entry.get("recclass", ""),
            "mass": float(entry["mass"]) if "mass" in entry else None,
            "fall": entry.get("fall", ""),
            "year": entry.get("year", ""),
            "reclat": float(entry["reclat"]) if "reclat" in entry else None,
            "reclong": float(entry["reclong"]) if "reclong" in entry else None,
            "point coordinates": coordinates
        }
        processed_data.append(processed_entry)

    # Step 3: Save the processed data as a CSV file
    try:
        with open("meteorite_data.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
            fieldnames = ["Name of Earth Meteorite", "id", "nametype", "recclass", "mass", "fall", "year", "reclat", "reclong", "point coordinates"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(processed_data)

        print("Data downloaded and converted to CSV successfully!")
    except IOError as e:
        print(f"An error occurred while writing the CSV file: {e}")

# Call the function to download and convert the data
download_and_convert_to_csv()
