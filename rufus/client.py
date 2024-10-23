class RufusClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def scrape(self, url, instructions):
        from .scraper import WebScraper
        from .synthesizer import DocumentSynthesizer

        scraper = WebScraper(url, instructions)
        content = scraper.crawl_and_scrape()
        synthesizer = DocumentSynthesizer()
        structured_document = synthesizer.synthesize(content)
        return structured_document
