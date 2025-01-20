import csv
import requests
import json

# Replace with your actual API key
api_key = 'TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J'


def fetch_sponsored_legislation(bioguide_id):
    base_url = f"https://api.congress.gov/v3/member/{bioguide_id}/sponsored-legislation?format=json&offset=0&limit=250&api_key={api_key}"

    while base_url:
        response = requests.get(base_url, headers={"accept": "application/json"})
        if response.status_code == 200:
            data = response.json()
            #print(data)
            print(base_url)
            print(bioguide_id)
            pagination = data.get('pagination', {})
            base_url = pagination.get('next')
            if base_url:
                base_url += f"&api_key={api_key}"

        else:
            print(f"Failed to fetch data for {bioguide_id}, status code: {response.status_code}")
            base_url = None

    return data


# Open the CSV file
with open('filtered_unique_members.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        bioguide_id = row['bioguideId']

        # Fetch the sponsored legislation data
        sponsored_legislation = fetch_sponsored_legislation(bioguide_id)

        # Write the data to an individual JSON file
        with open(f'sponsor_{bioguide_id}.json', 'w') as outfile:
            json.dump(sponsored_legislation, outfile, indent=4)
            print(sponsored_legislation)
            print(outfile)

