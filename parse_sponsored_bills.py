import os
import json
import csv

# Define the output CSV file
output_file = 'small_All_sponsors_data.csv'

# Specify the directory containing the JSON files
directory = '.'

# Define the CSV column headers
headers = ['bioguideid', 'congress', 'introducedDate', 'actionDate', 'text', 'number', 'policyArea', 'title', 'type',
           'url']

# Open the CSV file for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the headers to the CSV file
    csvwriter.writerow(headers)

    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file name starts with 'sponsor_'
        if filename.startswith('sponsor_') and filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(filename)
            # Open and read the JSON file
            with open(file_path, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)

                # Iterate over each record in the JSON data
                for record in data:
                    # Extract the required fields, handling missing data
                    bioguideid = filename.split('_')[1].split('.')[0]
                    congress = record.get('congress', '')
                    introducedDate = record.get('introducedDate', '')
                    latestAction = record.get('latestAction', {})
                    # If latestAction is null, set actionDate and text to null
                    if latestAction is None:
                        actionDate = None
                        text = None
                    else:
                        actionDate = latestAction.get('actionDate', '')
                        text = latestAction.get('text', '')
                    number = record.get('number', '')
                    policyArea = record.get('policyArea', {})
                    # If policyArea is null, set name to null
                    if policyArea is None:
                        name = None
                    else:
                        name = policyArea.get('name', '')
                    title = record.get('title', '')
                    bill_type = record.get('type', '')
                    url = record.get('url', '')

                    # Write the extracted data to the CSV file
                    csvwriter.writerow(
                        [bioguideid, congress, introducedDate, actionDate, text, number, policyArea, title, bill_type,
                         url])

print(f'Data has been successfully written to {output_file}')
