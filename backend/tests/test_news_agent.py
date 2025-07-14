import unittest
import logging
import os
import dotenv
from app.agents.news_agent import NewsAgent
from app.agents.task_planner import TaskPlanner
from app.core.embedding_client import EmbeddingClient
from app.core.llm_client import LLMClient
from app.core.web_scraper_client import WebScraperClient

# initialize env variables
dotenv.load_dotenv()

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize embedder, scraper, and llm
embedder = EmbeddingClient()
scraper = WebScraperClient()
llm_client = LLMClient(os.getenv("GROQ_API_KEY"))

class TestNewsAgent(unittest.TestCase):
    def setUp(self):
        self.news_agent = NewsAgent(embedder, scraper, llm_client)
        self.task_planner = TaskPlanner(embedder, llm_client)

    def test_search_GNEWS(self):
        query = "I want recent news about XRP"
        topic = self.task_planner.get_topic(query)
        logger.info(f"topic{topic}")
        logger.info(f"searching GNEWS")
        results = self.news_agent.search_GNEWS(topic=topic)
        logger.info(f"results: {results}")

    def test_summarize_news_article(self):
        query = "I want recent news about artificial intelligence"
        topic = self.task_planner.get_topic(query)
        logger.info(f"topic: {topic}")
        results = self.news_agent.search_GNEWS(topic=topic)
        logger.info(f"searching GNEWS")
        
        if results:
            article_url = results[0]["url"]
            logger.info(f"summarizing article url: {article_url}")
            summary = self.news_agent.summarize_news_article(article_url)
            logger.info(f"summary: {summary}")
        else:
            logger.warning("No articles found to summarize.")

if __name__ == "__main__":
    unittest.main()