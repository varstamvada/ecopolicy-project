import os
import json
import csv

directory = './all_sponsored_legislations'
output_csv = 'all_sponsored_bills.csv'
csv_headers = ['bioguideId', 'congress', 'type', 'number', 'introducedDate', 'actionDate', 'PolicyArea_name', 'Latest_Action_text', 'url', 'congress_type_number', 'title']
counter = 0
csv_rows = []

for filename in os.listdir(directory):
    if filename.startswith('sponsor_') and filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        print(filename)
        counter += 1
        print(counter)
        with open(file_path, 'r') as file:
            data = json.load(file)

        bioguide_id = data['request'].get('bioguideId', None)

        for item in data.get('sponsoredLegislation', []):
            congress = item.get('congress', None)
            type_ = item.get('type', None)
            number = item.get('number', None)
            introduced_date = item.get('introducedDate', None)
            latest_action = item.get('latestAction', {})
            # If latestAction is null, set actionDate and text to null
            if latest_action is None:
                action_date = None
                text = None
            else:
                action_date = latest_action.get('actionDate', '')
                text = latest_action.get('text', '')
            title = item.get('title', None)
            policy_area = item.get('policyArea', {})
            # If policyArea is null, set name to null
            if policy_area is None:
                name = None
            else:
                name = policy_area.get('name', '')
            url = item.get('url', None)
            congress_type_number = f"{congress}_{type_}_{number}"





            # Append the row to the CSV rows list
            csv_rows.append([
                bioguide_id, congress, type_, number, introduced_date, action_date, name, text, url, congress_type_number, title
            ])

# Write the CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csv_headers)
    csvwriter.writerows(csv_rows)

print(f"CSV file '{output_csv}' has been created successfully.")
