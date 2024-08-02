import json
import csv
import os


# Directory where the response files are saved
directory = "."

# Iterate over the range of offsets
for offset in range(0, 3000, 250):
    file_name = f"response_{offset}.json"
    file_path = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        # Open and read the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
        # Prepare the data to be written to CSV
        members_data = []
        for member in data['members']:
            bioguideId = member.get('bioguideId', '')
            district = member.get('district', '')
            partyName = member.get('partyName', '')
            state = member.get('state', '')
            name = member.get('name', '')

            terms = member.get('terms', {}).get('item', [])
            for term in terms:
                chamber = term.get('chamber', '')
                startYear = term.get('startYear', 0)
                endYear = term.get('endYear', 0) if term.get('endYear') else 0

                members_data.append({
                    'bioguideId': bioguideId,
                    'district': district,
                    'partyName': partyName,
                    'state': state,
                    'chamber': chamber,
                    'startYear': startYear,
                    'endYear': endYear,
                    'name': name
                })

        # Define the CSV file headers
        headers = ['bioguideId', 'district', 'partyName', 'state', 'chamber', 'startYear', 'endYear', 'name']

        # Write the data to CSV
        with open('extracteddata.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(members_data)

print("Data has been extracted and written to extracteddata.csv")
