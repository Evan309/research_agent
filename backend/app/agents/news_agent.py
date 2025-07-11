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
    def __init__(self, embedder, web_scraper, LLM_client):
        self.embedder = embedder
        self.GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
        self.web_scraper = web_scraper
        self.llm_client = LLM_client


    # search news with GNEWS api
    def search_GNEWS(self, topic: str, max_results: int = 10, sortby: str = "publishedAt") -> list[dict]:
        search_url = f"https://gnews.io/api/v4/search"
        params = {
            "q": topic,
            "token": self.GNEWS_API_KEY,
            "max": max_results,
            "sortby": sortby
        }
        logger.info(f"searching news with topic: {topic}")

        response = requests.get(search_url, params)

        # return list of articles
        data = response.json()
        logger.info(f"number of articles found: {data["totalArticles"]}")
        results = data["articles"]
        return results

    # summarize news articles by scraping article urls
    def summarize_news_article(self, article_url: str):
        logger.info(f"summarizing article url: {article_url}")

        # scrape article url for main content
        scraped_results = self.web_scraper.scrape_article_url(article_url)

        # summarize content with LLM



