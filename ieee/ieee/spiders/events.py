
import os
import json
import scrapy
from scrapy_splash import SplashRequest
from ieee.items import IeeeItem
        
class Events(scrapy.Spider):
    name = "events"

    # Custom settings for the spider
    custom_settings = {
        'DOWNLOAD_DELAY': 8,
        'CONCURRENT_REQUESTS': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
    }

    def start_requests(self):
        url = 'https://www.conferencelists.org/ieee/'
        yield SplashRequest(url, self.parse, args={'wait': 2})


    def parse(self, response):
        #check if response was successful
        if response.status == 200:
            print("Successfully fetched the webpage.")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status}")
            return
        
        #Extract conference data
        conferences = response.css('.wpem-event-listings .wpem-event-layout-wrapper .wpem-event-infomation .wpem-event-details')    
        
        # Initiated an empty list to hold extracted data 
        data = [] 
        
        for conference in conferences:
        # Extracted and stored the data in this item -check items.py
            item = IeeeItem()
            item['title'] = conference.css('.wpem-event-title h3::text').get()
            item['date'] = conference.css('span.wpem-event-date-text::text').get()
            item['location'] = conference.css('span.wpem-event-location-text::text').get()
            item['country'] = conference.css('span.wpem-event-type-text::text').get()
            item['link'] = conference.css('a.wpem-event-action-url::attr(href)').get()
            

            data.append(dict(item)) #Appended the item as a dictionary

            yield item

        # Wrote extracted data to this json file in a directory
        self.write_to_json(data)

    def write_to_json(self, data):
    # Defined the output directory and file path
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')) 
        output_dir = os.path.join(project_dir, '_data')
        output_file = os.path.join(output_dir, 'conferences.json')

        # Ensured the _data directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Wrote the data to the JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Data has been written to {output_file}")

