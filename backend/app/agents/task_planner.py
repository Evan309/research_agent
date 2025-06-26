import sentence_transformers as st
import logging

# Initialize logging
logger = logging.getLogger(__name__)

# Initialize the sentence transformer model
model = st.SentenceTransformer("all-MiniLM-L6-v2")

TASK_DESCRIPTIONS = {
    "find_papers": "search for research papers, academic articles, studies",
    "find_datasets": "search for datasets, data collections, corpora",
    "find_news": "search for news articles, recent updates, announcements",
}

# get subtasks matching the query using sentence transformers
def get_subtasks(query: str) -> list[str]:

    # encode the query using the sentence transformer model
    logger.info(f"Encoding query: {query}")
    query_emb = model.encode(query, convert_to_tensor=True)
    subtasks = []

    for task, description in TASK_DESCRIPTIONS.items():
        # encode task description
        logger.info(f"Encoding task description: {description}")
        task_emb = model.encode(description, convert_to_tensor=True)

        # calculate similarity
        logger.info(f"Calculating similarity between query and task: {task}")
        similarity = st.util.pytorch_cos_sim(query_emb, task_emb)
        logger.info(f"Similarity for task: {similarity.item()}")

        if similarity.item() > 0.5:
            subtasks.append(task)

    if not subtasks:
        subtasks = list(TASK_DESCRIPTIONS.keys())

    logger.info(f"Identified subtasks: {subtasks}")
    return subtasks

# # get topic matching the query using LLM
# def get_topic(query: str) -> str:

