import logging
import os
import dotenv

# initialize logging
logger = logging.getLogger(__name__)

# load environment variables
dotenv.load_dotenv()

class PaperAgent:
    def __init__(self, embedder, web_scraper, LLM_client):
        self.embedder = embedder
        self.web_scraper = web_scraper
        self.llm_client = LLM_client
        self.core_api_key = os.getenv("CORE_API_KEY")

    # search papers through CORE API
    def search_core_papers(self, topic: str, max_results: int = 10) -> list[dict]:
        pass