import unittest
import logging
from app.agents.paper_agent import PaperAgent

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestPaperAgent(unittest.TestCase):
    def setUp(self):
        self.agent = PaperAgent()
        self.topic = "machine learning"
        self.max_results = 5

    # test basic api call
    def test_search_core_papers(self):
        # search for papers related to the topic
        results = self.agent.search_core_papers(self.topic, self.max_results)

        # log results
        logger.info(f"Search results for topic '{self.topic}': {results}")


if __name__ == "__main__":
    unittest.main()