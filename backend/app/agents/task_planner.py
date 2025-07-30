import logging
from app.core.prompts import TOPIC_CLASSIFICATION_PROMPT

# Initialize logging
logger = logging.getLogger(__name__)


"""
embedding client is struggling to classify subtasks from user prompt. integrate llm "thought" into workflow. example workflow:
if max(similarity_score) < .35:
    call "thought" process through llm
"""
class TaskPlanner:
    def __init__(self, embedder, LLM_client):
        self.embedder = embedder
        self.llm_client = LLM_client
        self.task_descriptions = {
            "find_papers": "Find academic research papers, scientific studies, or scholarly articles related to the user's topic. Help the user read expert-written papers on the subject they’re interested in. Return reliable research from journals, universities, or conferences.",
            "find_datasets": "Find datasets, data collections, or CSV files that match the user's topic. Help the user locate public or open-source data they can download and analyze. Return structured data from portals, repositories, or research sources.",
            "find_news": "Get the latest news, headlines, or current events about the user's topic. Show what is happening right now in the world related to the subject. Return recent articles or news coverage from trusted sources."
        }

    # get subtasks matching the query using sentence transformers
    def get_subtasks(self, query: str) -> list[str]:

        # encode the query using the sentence transformer model
        logger.info(f"Encoding query: {query}")
        query_emb = self.embedder.encode(query, True)
        threshold = 0.35
        subtasks = []

        for task, description in self.task_descriptions.items():
            # encode task description
            logger.info(f"Encoding task description: {description}")
            task_emb = self.embedder.encode(description, True)

            # calculate similarity
            logger.info(f"Calculating similarity between query and task: {task}")
            similarity = self.embedder.similarity(query_emb, task_emb)

            if similarity.item() > threshold:
                subtasks.append(task)

        if not subtasks:
            logger.info("no tasks found adding all tasks")
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
