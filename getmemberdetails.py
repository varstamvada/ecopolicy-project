import csv
import requests
import json

# Define your API key and base URL
API_KEY = 'TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J'
BASE_URL = 'https://api.congress.gov/v3/member/'


# Function to get member details from the API
def get_member_details(bioguideid):
    url = f"{BASE_URL}{bioguideid}?format=json&api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        member_data = data.get('member', {})

        # Extract required fields
        bioguide_id = member_data.get('bioguideId', 'N/A')
        birth_year = member_data.get('birthYear', 'N/A')
        cosponsored_legislation_count = member_data.get('cosponsoredLegislation', {}).get('count', 'N/A')
        sponsored_legislation_count = member_data.get('sponsoredLegislation', {}).get('count', 'N/A')
        current_member = member_data.get('currentMember', 'N/A')
        inverted_order_name = member_data.get('invertedOrderName', 'N/A')
        terms_count = len(member_data.get('terms', []))
        start_year = member_data.get('terms', [{}])[0].get('startYear', 'N/A') if terms_count > 0 else 'N/A'

        # Return the extracted data
        return {
            'bioguideId': bioguide_id,
            'invertedOrderName': inverted_order_name,
            'currentMember': current_member,
            'terms': terms_count,
            'startYear': start_year,
            'birthYear': birth_year,
            'sponsoredLegislation': sponsored_legislation_count,
            'cosponsoredLegislation': cosponsored_legislation_count
        }
    else:
        print(f"Failed to retrieve data for bioguideId {bioguideid}. Status code: {response.status_code}")
        return None


# Read the CSV file and process each row
with open('old_files/orig_filtered_unique_members.csv', mode='r') as infile, open('memberdetails.csv', mode='w',
                                                                        newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Write the header row to the output file
    csv_writer.writerow(
        ['bioguideId', 'invertedOrderName', 'currentMember', 'terms', 'startYear', 'birthYear', 'sponsoredLegislation',
         'cosponsoredLegislation'])

    # Process each row from the input file
    for row in csv_reader:
        bioguideid = row[0]

        if bioguideid:
            print(f"Processing bioguideId: {bioguideid}")
            member_details = get_member_details(bioguideid)

            if member_details:
                # Write member details to output CSV
                csv_writer.writerow([
                    member_details['bioguideId'],
                    member_details['invertedOrderName'],
                    member_details['currentMember'],
                    member_details['terms'],
                    member_details['startYear'],
                    member_details['birthYear'],
                    member_details['sponsoredLegislation'],
                    member_details['cosponsoredLegislation']
                ])
            else:
                print(f"No data available for bioguideId: {bioguideid}")

print("Processing complete. Data has been written to memberdetails.csv.")
