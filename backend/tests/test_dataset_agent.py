import unittest
import logging
from app.agents.dataset_agent import DatasetAgent
from app.agents.task_planner import TaskPlanner

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestDatasetAgent(unittest.TestCase):
    def setUp(self):
        self.dataset_agent = DatasetAgent()
        self.task_planner = TaskPlanner()

    def test_search_kaggle_datasets(self):
        query = "I want to find datasets on credit score classification"
        topic = self.task_planner.get_topic(query)
        logger.info(f"topic: {topic}")
        logger.info(f"searching for datasets on kaggle")
        results = self.dataset_agent.search_kaggle_datasets(topic)
        logger.info(f"found {len(results)} datasets")
        logger.info(f"results: {results}")

    def test_get_kaggle_dataset_info(self):
        dataset_id = 5660999
        logger.info(f"getting dataset info for dataset id: {dataset_id}")
        results = self.dataset_agent.get_kaggle_dataset_info(dataset_id)
        logger.info(f"info for dataset {dataset_id}: {results}")
        

if __name__ == "__main__":
    unittest.main()
