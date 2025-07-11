import unittest
import logging
from app.agents.news_agent import NewsAgent
from app.agents.task_planner import TaskPlanner
from app.core.embedding_client import EmbeddingClient

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize embedder
embedder = EmbeddingClient()

class TestNewsAgent(unittest.TestCase):
    def setUp(self):
        self.news_agent = NewsAgent(embedder)
        self.task_planner = TaskPlanner(embedder)

    def test_search_GNEWS(self):
        query = "I want recent news about computer vision"
        topic = self.task_planner.get_topic(query)
        logger.info(f"topic{topic}")
        logger.info(f"searching GNEWS")
        results = self.news_agent.search_news(topic=topic)
        logger.info(f"results: {results}")


if __name__ == "__main__":
    unittest.main()