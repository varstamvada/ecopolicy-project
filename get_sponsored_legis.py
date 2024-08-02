import csv
import json
import requests

# Replace with your actual API key
api_key = 'TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J'

# Open the CSV file
with open('pullmemberbill.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        bioguide_id = row['bioguideId']

        # Construct the URL for the API request
        url = f"https://api.congress.gov/v3/member/{bioguide_id}/sponsored-legislation?format=json&offset=0&limit=250&api_key={api_key}"

        # Make the request
        response = requests.get(url, headers={"accept": "application/json"})

        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON response
            data = response.json()

            # Write the JSON data to an individual file
            with open(f'sponsor_{bioguide_id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        else:
            print(f"Failed to fetch data for {bioguide_id}, status code: {response.status_code}")

