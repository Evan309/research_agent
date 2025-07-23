import logging

# initialize logging
logger = logging.getLogger(__name__)

class Summarizer:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    # summarize results of subtasks
    def summarize(self, results: dict) -> str:
        logger.info(f"summarizing results: {results}")
        topic = results.get("topic", "your topic")

        response = [f"Here's what I found about **{topic}**:\n"]

        # parse papers if papers subtask was called
        if results.get("papers"):
            logger.info("parsing results from paper agent")
            papers = results.get("papers")
            response.append("**Research Papers**:")
            for paper in papers:
                title = paper.get("titile", "Untitled")
                summary = paper.get("summary", "No summary available")
                url = paper.get("pdfURL", "No url available")
                bullet = f"- **{title}** – {summary[:200]}{'...' if len(summary) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)
            
        # parse datasets if dataset subtask was called
        if results.get("datasets"):
            logger.info("parsing results from dataset agent")
            datasets = results.get("datasets")
            response.append("\n **Relevant Datasets**:")
            for dataset in datasets:
                title = dataset["title"]
                description = dataset["description"]
                url = dataset["url"]
                bullet = f"- **{title}** – {description[:200]}{'...' if len(description) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)

        # parse news if news subtask was called
        if results.get("news"):
            logger.info("parsing news from news agent")
            news = results.get("news")
            response.append("\n **Recent News**:")
            for article in news:
                title = article["title"]
                description = article["description"]
                url = article["url"]
                bullet = f"- **{title}** – {description[:200]}{'...' if len(description) > 200 else ''} {f'[{url}]' if url else ''}"
                response.append(bullet)

        return "\n".join(response).strip()
