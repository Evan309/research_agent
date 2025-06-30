import logging
import os 
import dotenv
from backend.app.core.llm_client import LLMClient
from backend.app.core.prompts import TOPIC_CLASSIFICATION_PROMPT

# load environment variables
dotenv.load_dotenv()

# Initialize logging
logger = logging.getLogger(__name__)

class TaskPlanner:
    def __init__(self, embedder):
        self.embedder = embedder
        self.llm_client = LLMClient(api_key=os.getenv("GROQ_API_KEY"))
        self.task_descriptions = {
            "find_papers": "search for research papers, academic articles, studies",
            "find_datasets": "search for datasets, data collections, corpora",
            "find_news": "search for news articles, recent updates, announcements",
        }

    # get subtasks matching the query using sentence transformers
    def get_subtasks(self, query: str) -> list[str]:

        # encode the query using the sentence transformer model
        logger.info(f"Encoding query: {query}")
        query_emb = self.embedder.encode(query, convert_to_tensor=True)
        subtasks = []

        for task, description in self.task_descriptions.items():
            # encode task description
            logger.info(f"Encoding task description: {description}")
            task_emb = self.embedder.encode(description, convert_to_tensor=True)

            # calculate similarity
            logger.info(f"Calculating similarity between query and task: {task}")
            similarity = self.embedder.similarity(query_emb, task_emb)
            logger.info(f"Similarity for task: {similarity.item()}")

            if similarity.item() > 0.5:
                subtasks.append(task)

        if not subtasks:
            subtasks = list(self.task_descriptions.keys())

        logger.info(f"Identified subtasks: {subtasks}")
        return subtasks
    

    # get topic matching the query using LLM
    def get_topic(self, query: str) -> str:
        # query the LLM to get the topic
        prompt = TOPIC_CLASSIFICATION_PROMPT.format(query=query)
        logger.info(f"retrieving topic for query: {query}")
        response = self.llm_client.generate_response(prompt, max_tokens=100)
        logger.info(f"topic: {response}")
        return response
