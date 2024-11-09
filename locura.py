import zipfile
import os
import csv
import json

# Path to the ZIP file
zip_file_path = 'C:/Users/sarab/Downloads/athletes.zip'
extract_dir = 'extracted_athletes'

# Step 1: Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Step 2: Process athlete data
athlete_data = []

# Function to process each athlete's CSV
def process_athlete(csv_file):
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

            # Extract the athlete's name and ID
            name = data[0][0]
            athlete_id = data[1][0]

            # Find the best time
            best_time_row = None
            best_time = None
            for row in data[3:]:
                if len(row) >= 6:
                    time_str = row[3]
                    try:
                        parts = time_str.split(':')
                        current_time = int(parts[0]) * 60 + float(parts[1])
                        if best_time is None or current_time < best_time:
                            best_time = current_time
                            best_time_row = row
                    except (ValueError, IndexError):
                        continue
            
            # If found, extract details
            if best_time_row:
                overall_place = best_time_row[1]
                time = best_time_row[3]
                date = best_time_row[4]
                meet = best_time_row[5] if len(best_time_row) > 5 else "N/A"
                comments = best_time_row[6] if len(best_time_row) > 6 and best_time_row[6] else "No comments for this race"
                picture = best_time_row[7] if len(best_time_row) > 7 and best_time_row[7] else None
            else:
                overall_place = "N/A"
                time = "N/A"
                date = "N/A"
                meet = "N/A"
                comments = "No valid time found"
                picture = None

            athlete_data.append({
                "name": name,
                "athlete_id": athlete_id,
                "overall_place": overall_place,
                "time": time,
                "date": date,
                "meet": meet,
                "comments": comments,
                "picture": picture
            })
    except FileNotFoundError:
        print(f"File {csv_file} not found.")

# Step 3: Iterate over all athletes
athlete_files = [f for f in os.listdir(os.path.join(extract_dir, 'mens_team')) if f.endswith('.csv')]

for athlete_file in athlete_files:
    csv_path = os.path.join(extract_dir, 'mens_team', athlete_file)
    process_athlete(csv_path)

# Step 4: Save athlete data as JSON
with open('athlete_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(athlete_data, json_file)

print("Athlete data saved as JSON.")