import logging

from app.core.prompts import SUMMARY_PROMPT

# initialize logging
logger = logging.getLogger(__name__)

class Summarizer:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    # query llm for summary
    def summarize_response(self, results: str, query: str) -> str:
        prompt = SUMMARY_PROMPT.format(query=query, results=results)
        summary = self.llm_client.generate_response(prompt)
        return summary

    # summarize results of subtasks
    def summarize(self, results: dict, query: str) -> str:
        logger.info(f"summarizing results: {results}")
        topic = results.get("topic", "your topic")

        response = [f"Here's what I found about **{topic}**:\n"]

        # parse papers if papers subtask was called
        if results.get("find_papers"):
            logger.info("parsing results from paper agent")
            papers = results.get("find_papers")
            response.append("**Research Papers**:")
            for paper in papers:
                title = paper.get("titile", "Untitled")
                summary = paper.get("summary", "No summary available")
                url = paper.get("pdfURL", "No url available")
                bullet = f"- **{title}** – {summary[:200]}{'...' if len(summary) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)
            
        # parse datasets if dataset subtask was called
        if results.get("find_datasets"):
            logger.info("parsing results from dataset agent")
            datasets = results.get("find_datasets")
            response.append("\n **Relevant Datasets**:")
            for dataset in datasets:
                title = dataset["title"]
                description = dataset["description"]
                url = dataset["url"]
                bullet = f"- **{title}** – {description[:200]}{'...' if len(description) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)

        # parse news if news subtask was called
        if results.get("find_news"):
            logger.info("parsing news from news agent")
            news = results.get("find_news")
            response.append("\n **Recent News**:")
            for article in news:
                title = article["title"]
                description = article["description"]
                url = article["url"]
                bullet = f"- **{title}** – {description[:200]}{'...' if len(description) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)

        summary = self.summarize_response(results, query)
        logger.info(f"final summary: {summary}")
        return summary
