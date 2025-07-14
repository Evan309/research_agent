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