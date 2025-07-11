import unittest
import logging
from app.core.web_scraper_client import WebScraperClient

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraperClient()

    def test_scrape_article_url(self):
        url = "https://theprint.in/brandstand/adon/rndr-whales-strengthen-positions-xrp-on-the-verge-of-breakout-blockdags-testnet-innovations-gain-developer-attention/2283627/"
        results = self.scraper.scrape_article_url(url)
        logger.info(f"web scraper results: {results}")


if __name__ == "__main__":
    unittest.main()