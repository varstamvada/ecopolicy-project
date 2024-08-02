
import json
count = 0

# Load JSON data from file
with open('responses.json', 'r') as file:
    data = json.load(file)

# Extract required information
members_info = []

for member in data['members']:
    bioguideId = member.get('bioguideId')
    district = member.get('district')
    partyName = member.get('partyName')
    state = member.get('state')
    name = member.get('name')

    # Extract terms information
    terms = member.get('terms', {}).get('item', [])
    for term in terms:
        chamber = term.get('chamber')
        endYear = term.get('endYear')
        startYear = term.get('startYear')

        member_info = {
            'bioguideId': bioguideId,
            'congressperson_name': name,
            'chamber': chamber,
            'partyName': partyName,
            'state': state,
            'district': district,
            'startYear': startYear,
            'endYear': endYear,
        }




        members_info.append(member_info)

# Print extracted information
for info in members_info:
    count += 1
    print(count, info)

