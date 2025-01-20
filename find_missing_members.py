import pandas as pd

# Load the CSV files into DataFrames
unique_members = pd.read_csv('./old_files/orig_filtered_unique_members.csv')
all_sponsored_bills = pd.read_csv('all_sponsored_bills.csv')

# Normalize the bioguideId values to lowercase for case-insensitive comparison
unique_members['bioguideId'] = unique_members['bioguideId'].str.lower()
all_sponsored_bills['bioguideId'] = all_sponsored_bills['bioguideId'].str.lower()

# Find bioguideId values present in unique_members but missing in all_sponsored_bills
missing_bioguide_ids = set(unique_members['bioguideId']) - set(all_sponsored_bills['bioguideId'])

# Output the missing bioguideIds
print("bioguideId values present in unique_members.csv but missing in all_sponsored_bills.csv:")
print(missing_bioguide_ids)

