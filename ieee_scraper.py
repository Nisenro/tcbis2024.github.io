import requests
from bs4 import BeautifulSoup
import json

# Define the URL
url = "https://www.ieee.org/"

# Custom headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Created a list to hold the extracted data
data = []

# Example: Extract and print the title of the page
title = soup.title.string
data.append({"type": "title", "content": title})

# Example: Extract and print all headings (h1, h2, h3, etc.)
for heading in soup.find_all(['h1', 'h2', 'h3']):
    data.append({"type": heading.name, "content": heading.get_text()})

# Example: Extract all links on the page
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.get_text()
    data.append({"type": "link", "text": text, "url": href})

# Write the data to a JSON file
json_file_path = '_data/conferences.json'
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Data has been written to conferences.json")

# Save data to JSON