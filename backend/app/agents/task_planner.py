import logging
from app.core.prompts import TOPIC_CLASSIFICATION_PROMPT

# Initialize logging
logger = logging.getLogger(__name__)

class TaskPlanner:
    def __init__(self, embedder, LLM_client):
        self.embedder = embedder
        self.llm_client = LLM_client
        self.task_descriptions = {
            "find_papers": "Get me research or scholarly publications. I want to read papers about this. Find articles written by experts or scientists.",
            "find_datasets": "Get me datasets related to this query. I'm looking for public data I can analyze. Help me find relevant data sources",
            "find_news": "I want the latest news on this topic. Get current events, announcements, or press coverage. Give me up-to-date headlines about this subject.",
        }

    # get subtasks matching the query using sentence transformers
    def get_subtasks(self, query: str) -> list[str]:

        # encode the query using the sentence transformer model
        logger.info(f"Encoding query: {query}")
        query_emb = self.embedder.encode(query, True)
        subtasks = []

        for task, description in self.task_descriptions.items():
            # encode task description
            logger.info(f"Encoding task description: {description}")
            task_emb = self.embedder.encode(description, True)

            # calculate similarity
            logger.info(f"Calculating similarity between query and task: {task}")
            similarity = self.embedder.similarity(query_emb, task_emb)

            if similarity.item() > 0.3:
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
