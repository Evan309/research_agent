TOPIC_CLASSIFICATION_PROMPT = """
Extract the main topic or subject from the following user query.  
Respond with only a few keywords (no explanation, no punctiation).

Query: "{query}"
Topic:
"""

ARTICLE_SUMMARIZATION_PROMPT = """
Summarize the following article into a clear and concise paragraph.
Focus on the main ideas and key points, and do not include any irrelevant information or commentary.
Only return the summary itself no additional text is needed.

Article:
\"\"\"
{content}
\"\"\"

Summary:
"""

SUMMARY_PROMPT = """
You are an assistant summarizing research agent results for a developer.
Given the following user query and results (papers, datasets, and news), write a 2-3 sentence summary that is clear and friendly.

Query: "{query}"
Results: {results_text}

Summary:
"""

REACT_TASK_PLANNER_PROMPT = """
You are an AI research assistant helping developers find resources for their projects.

Given a user's query, think step-by-step about what subtasks you should do to help them. Subtasks can include:
- find_papers: Search for academic papers, studies, or scientific articles
- find_datasets: Search for relevant datasets
- find_news: Search for recent news articles or announcements
- chat: Engage in friendly conversation, answer general or technical questions without retrieving external resources

Follow this format:

Query: "<user_query>"

Thought: Reason step-by-step about what the user is asking and what kind of help they want.

Subtasks: A Python list of subtasks (like ["find_papers", "find_datasets"]) that should be executed.
Only include relevant subtasks.

Examples:

Query: "What are some recent papers and datasets on wildfire detection?"
Thought: The user is looking for both research papers and datasets on wildfire detection. No need for news or chat.
Subtasks: ["find_papers", "find_datasets"]

Query: "Give me the latest news and data on electric vehicles"
Thought: The user is interested in recent events and data, so news and datasets are relevant.
Subtasks: ["find_datasets", "find_news"]

Now use this format to analyze the next query.

Query: "{query}"

Thought:
"""