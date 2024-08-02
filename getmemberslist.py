import requests
import json

# Your API key
api_key = "TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J"
# Base URL
base_url = "https://api.congress.gov/v3/member"
# Parameters
params = {
    "format": "json",
    "limit": 250,
    "fromDateTime": "2001-01-01T00:00:00Z",
    "api_key": api_key
}
# Headers
headers = {
    "accept": "application/json"
}

# Iterate over the offsets
for offset in range(0, 3000, 250):
    # Update offset parameter
    params["offset"] = offset
    # Send GET request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Write JSON to file
        with open(f"response_{offset}.json", "a") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Failed to get data for offset {offset}: {response.status_code}")

print("All data has been fetched and saved.")



