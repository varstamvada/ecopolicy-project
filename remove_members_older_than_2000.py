import pandas as pd

# Read the CSV file
file_path = 'unique_members.csv'
data = pd.read_csv(file_path)

# Filter the rows where endYear is 0 or higher than 2000
filtered_data = data[(data['endYear'] == 0) | (data['endYear'] > 2000)]

# Display the filtered data
print(filtered_data)

# Save the filtered data to a new CSV file (optional)
filtered_data.to_csv('filtered_unique_members.csv', index=False)
