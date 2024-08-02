import json
import os

# Directory where the response files are saved
directory = "."

# Iterate over the range of offsets
for offset in range(0, 3000, 250):
    file_name = f"response_{offset}.json"
    file_path = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        # Open and read the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
            # Process the data (e.g., print or manipulate)
            print(f"Data from {file_name}:")
            print(json.dumps(data, indent=4))
            print("\n")
    else:
        print(f"File {file_name} does not exist.")

print("All files have been processed.")

