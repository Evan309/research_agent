import logging
from kaggle.api.kaggle_api_extended import KaggleApi

# initialize logging
logger = logging.getLogger(__name__)

class DatasetAgent:
    def __init__(self, embedder):
        self.kaggle_api = KaggleApi()
        self.kaggle_api.authenticate()
        self.embedder = embedder

    # get kaggle datasets relevant to topic
    def search_kaggle_datasets(self, topic: str) -> list[dict]:
        results = self.kaggle_api.dataset_list(search=topic, sort_by="hottest")
        return results

    def search_huggingface_datasets(self, topic: str) -> list[dict]:
        pass
    
    # sort kaggle datasets by similiarity between title/subtitle and query using embeddings 
    def get_relevant_datasets(self, topic: str, datasets: list[dict]) -> list[dict]:
        filtered_datasets = []
        topic_embedding = self.embedder.encode(topic)

        logger.info(f"getting relevant datasets for topic: {topic}")
        for dataset in datasets:
            title_embedding = self.embedder.encode(dataset["title"])
            subtitle_embedding = self.embedder.encode(dataset["subtitle"])
            description_embedding = self.embedder.encode(dataset["description"])

            title_similarity = self.embedder.similarity(title_embedding, topic_embedding)
            subtitle_similarity = self.embedder.similarity(subtitle_embedding, topic_embedding)
            description_similarity = self.embedder.similarity(description_embedding, topic_embedding)
            similarity_score = (title_similarity + subtitle_similarity + description_similarity) / 3
            dataset["similarity_score"] = similarity_score
            filtered_datasets.append(dataset)

        # sort datasets by similarity score
        filtered_datasets.sort(key=lambda x: x["similarity_score"], reverse=True)
        return filtered_datasets



    
    def get_huggingface_dataset_info(self, dataset_id: str):
        pass
    
    def get_dataset_files(self, dataset_id: str):
        pass