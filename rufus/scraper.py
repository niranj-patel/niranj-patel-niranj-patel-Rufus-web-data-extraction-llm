import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url, instructions):
        self.url = url
        self.instructions = instructions

    def crawl_and_scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Scraping logic here
        return soup
