import unittest
import logging
import os
from dotenv import load_dotenv
from app.agents.summarizer import Summarizer
from app.agents.news_agent import NewsAgent
from app.agents.dataset_agent import DatasetAgent
from app.agents.paper_agent import PaperAgent
from app.agents.task_planner import TaskPlanner
from app.core.embedding_client import EmbeddingClient
from app.core.llm_client import LLMClient
from app.core.web_scraper_client import WebScraperClient

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize env variables
load_dotenv()

# initialize embedder, scraper, and llm
embedder = EmbeddingClient()
scraper = WebScraperClient()
llm_client = LLMClient()

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = Summarizer(llm_client)
        self.dataset_agent = DatasetAgent(embedder)
        self.paper_agent = PaperAgent(llm_client)
        self.news_agent = NewsAgent(embedder, scraper, llm_client)
        self.task_planner = TaskPlanner(embedder, llm_client)
        self.subtask_map = {
            "find_papers": lambda topic: self.paper_agent.search_core_papers(topic),
            "find_datasets": lambda topic: self.dataset_agent.search_kaggle_datasets(topic),
            "find_news": lambda topic: self.news_agent.search_GNEWS(topic)
        }

    def test_summarize(self):
        logger.info("testing summarize")

        # store results
        results = {}

        # prompt
        prompt = "Show me recent research on transformer models in NLP."

        # get subtasks and topic
        topic = self.task_planner.get_topic(prompt)
        subtasks = self.task_planner.get_subtasks(prompt)
        results["topic"] = topic

        # execute subtasks
        logger.info(f"executing subtasks: {subtasks}")
        for subtask in subtasks:
            if subtask in self.subtask_map:
                try:
                    logger.info(f"attempting to execute subtask: {subtask}")
                    results[subtask] = self.subtask_map[subtask](topic)
                    logger.info(f"{subtask} completed with results: {results[subtask]}")
                except Exception as e:
                    logger.error(f"Error executing {subtask}: {e}")

            else:
                logger.info(f"{subtask} not done")

        # summarize results of all tasks
        summary = self.summarizer.summarize(results)
        logger.info(f"completed output: {summary}")


if __name__ == "__main__":
    unittest.main()