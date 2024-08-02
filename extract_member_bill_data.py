import json
import csv
import os

# Directory containing the sponsor files
directory = '.'

# Output CSV file
output_csv = 'sponsored_legislation.csv'

# CSV column headers
headers = ['bioguideid', 'congress', 'introduceddate', 'actiondate', 'text', 'number', 'policyArea name', 'title',
           'type', 'url']


# Function to extract data from JSON and write to CSV
def extract_data_to_csv(directory, output_csv):
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()

        # Iterate over each file in the directory
        for filename in os.listdir(directory):
            if filename.startswith('sponsor') and filename.endswith('.json'):
                file_path = os.path.join(directory, filename)

                # Read and parse JSON content
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)

                    bioguide_id = data['request']['bioguideId']
                    for legislation in data['sponsoredLegislation']:
                        row = {
                            'bioguideid': bioguide_id,
                            'congress': legislation.get('congress'),
                            'introduceddate': legislation.get('introducedDate'),
                            'actiondate': legislation['latestAction'].get('actionDate'),
                            'text': legislation['latestAction'].get('text'),
                            'number': legislation.get('number'),
                            'policyArea name': legislation['policyArea'].get('name'),
                            'title': legislation.get('title'),
                            'type': legislation.get('type'),
                            'url': legislation.get('url')
                        }
                        writer.writerow(row)


# Execute the function
extract_data_to_csv(directory, output_csv)
