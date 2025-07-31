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