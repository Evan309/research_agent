import sentence_transformers as st
import logging

# Initialize logging
logger = logging.getLogger(__name__)


class TaskPlanner:
    def __init__(self, model: str = "all-MiniLM-L6-v2"):
        self.model = st.SentenceTransformer(model)
        self.task_descriptions = {
            "find_papers": "search for research papers, academic articles, studies",
            "find_datasets": "search for datasets, data collections, corpora",
            "find_news": "search for news articles, recent updates, announcements",
        }

    # get subtasks matching the query using sentence transformers
    def get_subtasks(self, query: str) -> list[str]:

        # encode the query using the sentence transformer model
        logger.info(f"Encoding query: {query}")
        query_emb = self.model.encode(query, convert_to_tensor=True)
        subtasks = []

        for task, description in self.task_descriptions.items():
            # encode task description
            logger.info(f"Encoding task description: {description}")
            task_emb = self.model.encode(description, convert_to_tensor=True)

            # calculate similarity
            logger.info(f"Calculating similarity between query and task: {task}")
            similarity = st.util.pytorch_cos_sim(query_emb, task_emb)
            logger.info(f"Similarity for task: {similarity.item()}")

            if similarity.item() > 0.5:
                subtasks.append(task)

        if not subtasks:
            subtasks = list(self.task_descriptions.keys())

        logger.info(f"Identified subtasks: {subtasks}")
        return subtasks
    

    # get topic matching the query using LLM
    def get_topic(self, query: str) -> str:
        pass