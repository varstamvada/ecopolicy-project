import csv
import requests
from datetime import datetime

api_key = "TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J"
base_url = "https://api.congress.gov/v3/bill"

with open('non-environment.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Print out the fieldnames for debugging purposes
    print("CSV Column Names:", reader.fieldnames)

    rows = [row for row in reader]

# Define the correct column name with leading/trailing spaces removed
introduced_date_column = 'introducedDate'

# Check if the column exists in the CSV
if introduced_date_column not in rows[0]:
    print(f"Column '{introduced_date_column}' not found in CSV file.")
else:
    # Process each row
    for row in rows:
        introduced_date = row[introduced_date_column].strip()
        if introduced_date and datetime.strptime(introduced_date, "%Y-%m-%d") > datetime(2000, 1, 1):
            congress = row['congress'].strip()
# why is this case sensitive
            bill_type = row['type'].strip().lower()
            bill_number = row['number'].strip()

            # Construct the API URL
            api_url = f"{base_url}/{congress}/{bill_type}/{bill_number}/text?format=json&api_key={api_key}"

            # Make the API call
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()

                # Check if the textVersions are available
                if data.get('textVersions'):
                    for version in data['textVersions']:
                        for format in version['formats']:
                            if format['type'] == 'Formatted Text':
                                text_url = format['url']

                                # Fetch the text from the URL
                                text_response = requests.get(text_url)
                                if text_response.status_code == 200:
                                    text_content = text_response.text

                                    # Create the file name
                                    file_name = f"BILLS-{congress}{bill_type}{bill_number}.txt"

                                    # Save the text content to a file
                                    with open(file_name, 'w') as file:
                                        file.write(text_content)
                                    print(f"File {file_name} created successfully.")
                                else:
                                    print(f"Failed to fetch text from {text_url}")
                else:
                    print(f"No text versions available for bill {bill_number} in congress {congress}.")
            else:
                print(f"Failed to fetch data from {api_url}")
