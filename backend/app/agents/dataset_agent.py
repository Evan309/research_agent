import logging
from kaggle.api.kaggle_api_extended import KaggleApi

# initialize logging
logger = logging.getLogger(__name__)

class DatasetAgent:
    def __init__(self):
        self.kaggle_api = KaggleApi()
        self.kaggle_api.authenticate()

    def search_kaggle_datasets(self, topic: str) -> list[dict]:
        results = self.kaggle_api.datasets.search_datasets(query=topic)
        return results

    def search_huggingface_datasets(self, topic: str) -> list[dict]:
        pass
    
    def get_dataset_info(self, dataset_id: str):
        pass
    
    def get_dataset_files(self, dataset_id: str):
        pass