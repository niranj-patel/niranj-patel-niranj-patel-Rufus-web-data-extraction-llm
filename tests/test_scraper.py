import unittest
from rufus.scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def test_crawl_and_scrape(self):
        scraper = WebScraper("https://www.sfgov.com", "We're making a chatbot for the HR in San Francisco.")
        content = scraper.crawl_and_scrape()
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()
