import logging
from app.core.prompts import TOPIC_CLASSIFICATION_PROMPT
from app.core.prompts import REACT_TASK_PLANNER_PROMPT
from app.core.utils import extract_subtask_list

# Initialize logging
logger = logging.getLogger(__name__)


class TaskPlanner:
    def __init__(self, embedder, LLM_client):
        self.embedder = embedder
        self.llm_client = LLM_client
        self.chat_examples = [
            "How are you today?",
            "Tell me a joke.",
            "What's your name?",
            "Give me some tips for learning Python.",
            "What's trending in tech?"
        ]
        self.research_examples = [
            "Find recent papers on AI alignment.",
            "I need a dataset on income inequality.",
            "Give me news articles about quantum computing.",
            "What are the latest studies on climate change?",
            "Search for research on protein folding."
        ]
        self.chat_emb = [self.embedder.encode(e) for e in self.chat_examples]
        self.research_emb = [self.embedder.encode(e) for e in self.research_examples]
        self.task_descriptions = {
            "find_papers": "Find academic research papers, scientific studies, or scholarly articles related to the user's topic. Help the user read expert-written papers on the subject they’re interested in. Return reliable research from journals, universities, or conferences.",
            "find_datasets": "Find datasets, data collections, or CSV files that match the user's topic. Help the user locate public or open-source data they can download and analyze. Return structured data from portals, repositories, or research sources.",
            "find_news": "Get the latest news, headlines, or current events about the user's topic. Show what is happening right now in the world related to the subject. Return recent articles or news coverage from trusted sources."
        }

    # classify user prompt intent (chat or research) using embeddings
    def classify_intent(self, query: str) -> str:
        # encode query
        query_emb = self.embedder.encode(query)

        # compute similarity
        chat_similarity = [self.embedder.similarity(query_emb, e) for e in self.chat_emb]
        research_similarity = [self.embedder.similarity(query_emb, e) for e in self.research_emb]

        # compute average
        chat_avg = sum([sim.item() for sim in chat_similarity]) / len(chat_similarity)
        research_avg = sum([sim.item() for sim in research_similarity]) / len(research_similarity)

        return "chat" if chat_avg > research_avg else "research"

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
            logger.info("no tasks found from embeddings, pivoting to thought process in REACT")
            subtasks = self.llm_thought(query)

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
    
    # query llm to think about query and return subtasks
    def llm_thought(self, query: str) -> list[str]:
        # format prompt and call llm
        prompt = REACT_TASK_PLANNER_PROMPT.format(query=query)
        response = self.llm_client.generate_response(prompt, 256, 0.3)

        # prase subtasks into list format
        subtasks = extract_subtask_list(response)
        return subtasks
