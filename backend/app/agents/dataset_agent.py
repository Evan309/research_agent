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
    def search_kaggle_datasets(self, topic: str, num_datasets: int = 10) -> list[dict]:
        # search kaggle datasets for topic
        logger.info(f"searching kaggle datasets for topic: {topic}")
        results = self.kaggle_api.dataset_list(search=topic, sort_by="hottest")
        logger.info(f"found {len(results)} datasets")

        # parse kaggle datasets
        parsed_datasets = [self.parse_kaggle_dataset(dataset) for dataset in results]
        logger.info(f"parsed {len(parsed_datasets)} datasets")

        # get relevant datasets
        relevant_datasets = self.get_relevant_kaggle_datasets(topic, parsed_datasets)
        logger.info(f"found {len(relevant_datasets)} relevant datasets")

        # return relevant datasets
        logger.info(f"returning {num_datasets} relevant datasets")
        if num_datasets > len(relevant_datasets):
            return relevant_datasets
        else:
            return relevant_datasets[:num_datasets]

    def search_huggingface_datasets(self, topic: str) -> list[dict]:
        pass
    
    # sort kaggle datasets by similiarity between title/subtitle and query using embeddings 
    def get_relevant_kaggle_datasets(self, topic: str, datasets: list[dict]) -> list[dict]:
        filtered_datasets = []
        topic_embedding = self.embedder.encode(topic)

        logger.info(f"getting relevant datasets for topic: {topic}")
        for dataset in datasets:
            title_embedding = self.embedder.encode(dataset["title"])
            subtitle_embedding = self.embedder.encode(dataset["subtitle"])
            description_embedding = self.embedder.encode(dataset["description"])

            # calculate similarity between dataset and topic
            logger.info(f"calculating similarity between dataset: {dataset['title']} and topic: {topic}")
            title_similarity = self.embedder.similarity(title_embedding, topic_embedding)
            logger.info(f"calculating similarity between subtitle: {dataset['subtitle']} and topic: {topic}")
            subtitle_similarity = self.embedder.similarity(subtitle_embedding, topic_embedding)
            logger.info(f"calculating similarity between description: {dataset['description']} and topic: {topic}")
            description_similarity = self.embedder.similarity(description_embedding, topic_embedding)

            # calculate similarity score
            logger.info(f"calculating similarity score for dataset: {dataset['title']}")
            relevant_factors = title_similarity.item() + subtitle_similarity.item() + description_similarity.item() + dataset["download_count"] + dataset["usability_rating"]
            similarity_score = relevant_factors / 5
            dataset["similarity_score"] = similarity_score
            filtered_datasets.append(dataset)

        # sort datasets by similarity score
        filtered_datasets.sort(key=lambda x: x["similarity_score"], reverse=True)
        return filtered_datasets

    
    def get_huggingface_dataset_info(self, dataset_id: str):
        pass

    # parse kaggle dataset object to dict
    def parse_kaggle_dataset(self, dataset: dict) -> dict:
        logger.info(f"parsing kaggle dataset: {dataset.title}")
        dataset_info = {
            "title": dataset.title,
            "subtitle": dataset.subtitle,
            "description": dataset.description,
            "url": dataset.url,
            "download_count": dataset.download_count,
            "usability_rating": dataset.usability_rating,
        }
        logger.info(f"parsed kaggle dataset: {dataset_info}")
        return dataset_info
    

    def get_dataset_files(self, dataset_id: str):
        pass