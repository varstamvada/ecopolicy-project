import os
import json
import csv

# Define the columns for the CSV file
csv_columns = ['bioguideid', 'congress', 'introduceddate', 'actiondate', 'text', 'number', 'policyArea name', 'title', 'type', 'url']
csv_file = "legislation_sponsored.csv"

# Function to extract data from JSON and write to CSV
def json_to_csv(json_data, csv_writer):
    bioguideid = json_data['request']['bioguideId']
    for item in json_data['sponsoredLegislation']:
        row = {
            'bioguideid': bioguideid,
            'congress': item.get('congress', ''),
            'introduceddate': item.get('introducedDate', ''),
            'actiondate': item['latestAction'].get('actionDate', ''),
            'text': item['latestAction'].get('text', ''),
            'number': item.get('number', ''),
            'title': item.get('title', ''),
            'type': item.get('type', ''),
            'url': item.get('url', '')
        }
        csv_writer.writerow(row)

# Create and write to CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

    # Iterate through files in the current directory
    for filename in os.listdir('.'):
        if filename.startswith('sponsor_'):
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                json_to_csv(data, writer)

print(f"Data successfully written to {csv_file}")
