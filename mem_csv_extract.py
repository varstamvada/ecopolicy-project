import json
import csv

# Load the JSON data from the file
with open('mem.json', 'r') as file:
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
with open('extracteddata.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(members_data)

print("Data has been extracted and written to extracteddata.csv")
