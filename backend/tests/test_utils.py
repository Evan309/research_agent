import unittest
import logging
from app.core.utils import chunk_text_by_tokens
from app.core.web_scraper_client import WebScraperClient

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraperClient()

    def test_chunk_text_by_tokens(self):
        # scrape url
        url = "https://theprint.in/brandstand/adon/rndr-whales-strengthen-positions-xrp-on-the-verge-of-breakout-blockdags-testnet-innovations-gain-developer-attention/2283627/"
        results = self.scraper.scrape_article_url(url)
        logger.info(f"web scraper results: {results}")

        # retrieve scraped content
        content = results["content"]
        logger.info(f"attempting to chunk text: {content}")
        
        # chunk content
        chunks = chunk_text_by_tokens(content)
        logger.info(f"chunks: {chunks}")


if __name__ == "__main__":
    unittest.main()