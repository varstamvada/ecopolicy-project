import csv
import requests
import json
import math

# this replaces the get_sponsored_legis. This is the script that fetches all the bills for members

api_key = 'TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J'
limit = 250
base_url = 'https://api.congress.gov/v3/member/'
endpoint = 'sponsored-legislation?format=json'

def fetch_legis(bioguide_id):
    my_url = f"{base_url}{bioguide_id}/{endpoint}&offset=0&limit={limit}&api_key={api_key}"
    all_json = []
    r = requests.get(my_url)
    response = r.json()
    count = response['pagination']['count']
    print("count is", count)
    offset = 0
    count_num = int(count)
    pages = 1 + math.floor(count_num/limit)
    print("pages are", pages)
    for x in range(0, pages):
        final_url = f"{base_url}{bioguide_id}/{endpoint}&offset={offset}&limit={limit}&api_key={api_key}"
        offset = offset + limit
        #print(offset)
        #print(final_url)
        response = requests.get(final_url)
        dump = response.json()
        count_of_bills = str((dump['pagination']['count']))
        #all_json = dump
        all_json.extend(dump['sponsoredLegislation'])

    with open(f'sponsor_{bioguide_id}.json', 'w') as outfile:
        json.dump(all_json, outfile, indent=4)
        print(outfile)

    return final_url

#bioguide_id = 'L000174'
#bioguide_id = 'B001283'
#fetch_legis(bioguide_id)

#Open the CSV file
with open('old_files/limit_filtered_unique_members.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        bioguide_id = row['bioguideId']
       # Fetch the sponsored legislation data
        fetch_legis(bioguide_id)


#print(final_url)




