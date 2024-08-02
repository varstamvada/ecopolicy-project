import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('extracteddata.csv')

# Drop the first occurrence of any duplicate bioguideId
df = df.drop_duplicates(subset='bioguideId', keep='last')

# Save the modified DataFrame back to the CSV file
df.to_csv('extracteddata.csv', index=False)

print("Duplicates removed and file saved.")
