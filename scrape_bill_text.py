import requests
from bs4 import BeautifulSoup

# Replace with the URL you want to scrape
url = "https://www.congress.gov/117/bills/hr8404/BILLS-117hr8404enr.htm"

# Fetch the HTML content
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract all text content
    text = soup.get_text(separator="\n")  # Separate text with newlines

    # Print or use the extracted text
    print(text)
else:
    print("Error: Could not retrieve the content from the URL.")
