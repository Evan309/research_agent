import sentence_transformers as st

model = st.SentenceTransformer("all-MiniLM-L6-v2")

TASK_DESCRIPTIONS = {
    "find_papers": "search for research papers, academic articles, studies",
    "find_datasets": "search for datasets, data collections, corpora",
    "find_news": "search for news articles, recent updates, announcements",
}

# get subtasks matching the query
def get_subtasks(query: str) -> list[str]:

    # encode the query using the sentence transformer model
    query_emb = model.encode(query, convert_to_tensor=True)
    subtasks = []

    for task, description in TASK_DESCRIPTIONS.items():
        # encode task description
        task_emb = model.encode(description, convert_to_tensor=True)

        # calculate similarity
        similarity = st.util.pytorch_cos_sim(query_emb, task_emb)

        if similarity.item() > 0.5:
            subtasks.append(task)

    if not subtasks:
        subtasks = list(TASK_DESCRIPTIONS.keys())

    return subtasks

# get topic matching the query
def get_topic(query: str) -> str:
    