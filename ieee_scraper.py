import requests
from bs4 import BeautifulSoup
import json
import os

# Define the URLs
urls = [
    "https://www.conferencelists.org/ieee/",
    "https://www.conferencelists.org/ieee/page/2/"
]

# Custom headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Created a list to hold the extracted data
data = []

# Iterate through each URL and scrape the data
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully fetched the webpage: {url}")
    else:
        print(f"Failed to retrieve the webpage: {url}. Status code: {response.status_code}")
        continue

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all event details containers
    events = soup.find_all('div', class_='wpem-event-details')

    for event in events:
        try:
            title = event.find('div', class_='wpem-event-title').get_text(strip=True)
            date = event.find('span', class_='wpem-event-date-text').get_text(strip=True)
            location = event.find('span', class_='wpem-event-location-text').get_text(strip=True)
            
            link_tag = event.find('a', class_='wpem-event-action-url')
            if link_tag:
                link = link_tag['href']
            else:
                print(f"No link found for event: {title}")
                link = "#"

            # Append the event details to the data list
            data.append({
                "title": title,
                "date": date,
                "location": location,
                "link": link
            })
        except Exception as e:
            print(f"An error occurred while processing an event: {e}")
            continue

# Path to the JSON file
json_file_path = '_data/conferences.json'

# Write the data to the JSON file
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Data has been written to {json_file_path}")

# Path to the Markdown file
markdown_file_path = 'conferences.md'

# Check if the markdown file exists
if os.path.exists(markdown_file_path):
    mode = 'a'  # Append mode
else:
    mode = 'w'  # Write mode

# Read the JSON data and write it to the markdown file
with open(markdown_file_path, mode, encoding='utf-8') as f:
    # Write the title for the markdown file
    if mode == 'w':
        f.write("# Conferences\n\n")
    
    # Loop through each conference and format the data as markdown
    for conference in data:
        title = conference.get('title', 'N/A')
        date = conference.get('date', 'N/A')
        location = conference.get('location', 'N/A')
        link = conference.get('link', '#')

        # Write the conference details to the markdown file
        f.write(f"## {title}\n")
        f.write(f"- Date: {date}\n")
        f.write(f"- Location: {location}\n")
        f.write(f"- Link: [More Info]({link})\n\n")

print(f"Data has been appended to {markdown_file_path}")
