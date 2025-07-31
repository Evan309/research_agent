import unittest
import logging
import os
import dotenv
from app.agents.task_planner import TaskPlanner
from app.core.embedding_client import EmbeddingClient
from app.core.llm_client import LLMClient

# load environment variables
dotenv.load_dotenv()

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#initialize embedder and llm
embedder = EmbeddingClient()
llm_client = LLMClient()

class TestTaskPlanner(unittest.TestCase):
    def setUp(self):
        self.task_planner = TaskPlanner(embedder, llm_client)

    def test_get_subtasks(self):
        logger.info("testing get_subtasks")
        query = "I want to find research papers and datasets on credit score classification"
        subtasks = self.task_planner.get_subtasks(query)
        logger.info(f"subtasks: {subtasks}")

    def test_get_topic(self):
        logger.info("testing get_topic")
        query = "I want to find research papers on machine learning"
        topic = self.task_planner.get_topic(query)
        logger.info(f"topic: {topic}")

    def test_classify_intent(self):
        logger.info("testing classify intent")
        query = "I want to find research papers on machine learning"
        query2 = "Who is the current president"
        intent = self.task_planner.classify_intent(query)
        intent2 = self.task_planner.classify_intent(query2)
        logger.info(f"intent: {intent}")
        logger.info(f"intent2: {intent2}")


if __name__ == "__main__":
    unittest.main()
