import requests
from bs4 import BeautifulSoup
import json

# Define the URLs
urls = [
    "https://www.conferencelists.org/ieee/",
    "https://www.conferencelists.org/ieee/page/2/"
]

# Custom headers to mimic a browser visit
HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

# Create a list to hold the extracted data
data = []

# Iterate through each URL and scrape the data
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url, headers=HEADERS)

    
    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully fetched the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        exit()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Create a list to hold the extracted data
data = []

# Example: Extract and print the title of the page
title = soup.title
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
with open('_data/conferences.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Data has been written to conferences.json")