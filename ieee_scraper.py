import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime 

url = "https://www.ieee.org/"

response =requests.get(url)  #this sends a GET request to the url

if response.status_code == 200:
    print("Successfully fetched the webpage")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

data = [] #created an empty list to hold extracted data


# Extract the title
title = soup.title.string if soup.title else "No title found"
data.append({"type": "title", "content": title})

# Extract the specific "Upcoming conferences" link
upcoming_conferences_link = soup.find('a', string='Upcoming conferences')

if upcoming_conferences_link:
    href = upcoming_conferences_link.get('href')
    text = upcoming_conferences_link.get_text()
    data.append({"type": "link", "text": text, "url": href})
else:
    print("No 'Upcoming conferences' link found.")

# Save data to JSON
json_file_path = '_data/conferences.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data has been written to JSON file")