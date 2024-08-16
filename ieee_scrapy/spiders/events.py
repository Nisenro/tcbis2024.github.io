import scrapy
from scrapy_splash import SplashRequest 
import os
import json
from sys import path

path.append('C:\Users\adegb\Desktop\tcbis')

from ieee_scrapy.items import IeeeScrapyItem

class Events(scrapy.Spider):
    name = "events"
    def start_requests(self):
        url = 'https://www.conferencelists.org/ieee/'
        yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        conferences = response.css('.wpem-event-listings .wpem-event-layout-wrapper .wpem-event-infomation .wpem-event-details')    
        
        # Initiated an empty list to hold extracted data 
        data = []
        
        
        for conference in conferences:
        # Extracted and stored the data in this list
            conference_data = {
                'title': conference.css('.wpem-event-title h3::text').get(),
                'date': conference.css('span.wpem-event-date-text::text').get(),
                'location': conference.css('span.wpem-event-location-text::text').get(),
                'country': conference.css('span.wpem-event-type-text::text').get(),
                'link': conference.css('a.wpem-event-action-url::attr(href)').get()
            }

            data.append(conference_data)

            yield conference_data

            # Wrote extracted data to this json file in a directory
            self.write_to_json(data)

            # Check if the request was successful
        if response.status == 200:
            print("Successfully fetched the webpage.")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status}")
            exit()

    def write_to_json(self, data):
    # Define the output directory and file path
        output_dir = 'C:\\Users\\adegb\\Desktop\\tcbis\\_data'
        output_file = os.path.join(output_dir, 'conferences.json')

        # Ensure the _data directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Write the data to the JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Data has been written to {output_file}")

