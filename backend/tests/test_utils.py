import unittest
import logging
import os
import dotenv
from app.core.utils import chunk_text_by_tokens
from app.core.utils import summarize_chunks
from app.core.web_scraper_client import WebScraperClient
from app.core.llm_client import LLMClient

# load environment variables
dotenv.load_dotenv()

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize llm and scraper
scraper = WebScraperClient()
llm_client = LLMClient(os.getenv("GROQ_API_KEY"))

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.scraper = scraper
        self.llm_client = llm_client

        # scrape url
        self.url = "https://theprint.in/brandstand/adon/rndr-whales-strengthen-positions-xrp-on-the-verge-of-breakout-blockdags-testnet-innovations-gain-developer-attention/2283627/"
        self.results = self.scraper.scrape_article_url(self.url)
        logger.info(f"web scraper results: {self.results}")

    def test_chunk_text_by_tokens(self):
        # retrieve scraped content
        content = self.results["content"]
        logger.info(f"attempting to chunk text: {content}")
        
        # chunk content
        chunks = chunk_text_by_tokens(content)
        logger.info(f"number of chunks: {len(chunks)}")
        logger.info(f"chunks: {chunks}")

    def test_summarize_chunks(self):
         # retrieve scraped content
        content = self.results["content"]
        logger.info(f"attempting to chunk text: {content}")
        
        # chunk content
        chunks = chunk_text_by_tokens(content)
        logger.info(f"number of chunks: {len(chunks)}")
        logger.info(f"chunks: {chunks}")

        # summarize chunks
        summary = summarize_chunks(chunks, self.llm_client)
        logger.info(f"summary: {summary}")

if __name__ == "__main__":
    unittest.main()