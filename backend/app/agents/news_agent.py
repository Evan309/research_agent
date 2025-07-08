# search news agents and return the latest news about the research topic
import logging
import os
import requests
from dotenv import load_dotenv

# initialize logging
logger = logging.getLogger(__name__)

# load environment variables
load_dotenv()


class NewsAgent:
    def __init__(self, embedder):
        self.embedder = embedder
        self.GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

    def search_news(self, topic: str, max: int = 10, sortby: str = "publishedAt"):
        logger.info(f"searching nes with topic: {topic}")
        
        pass

    def summarize_news_article(self, article_url: str):
        pass


