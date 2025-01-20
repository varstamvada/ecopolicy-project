import pandas as pd

# Read the CSV files
bills_file_path = 'all_sponsored_bills.csv'
members_file_path = 'unique_members.csv'

bills_data = pd.read_csv(bills_file_path)
members_data = pd.read_csv(members_file_path)

# Count the number of rows by bioguideId from all_sponsored_bills.csv
bill_counts = bills_data['bioguideId'].value_counts().reset_index()
bill_counts.columns = ['bioguideId', 'row_count']

# Merge the bill_counts with the unique_members.csv on bioguideId
merged_data = pd.merge(bill_counts, members_data[['bioguideId', 'name']], on='bioguideId', how='left')

# Reorder columns as specified
result = merged_data[['bioguideId', 'name', 'row_count']]

# Save the result to a new CSV file
result.to_csv('number_bills_by_members.csv', index=False)
