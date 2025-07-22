import logging
import os
import dotenv
import requests
from app.core.utils import chunk_text_by_tokens, summarize_chunks 

# initialize logging
logger = logging.getLogger(__name__)

# load environment variables
dotenv.load_dotenv()



'''
search papers using the following apis
semantic scholar
core api
OpenAlex
'''
class PaperAgent:
    def __init__(self, LLM_client):
        self.llm_client = LLM_client
        self.core_api_key = os.getenv("CORE_API_KEY")

    # search papers through CORE API
    def search_core_papers(self, topic: str, max_results: int = 10) -> list[dict]:
        # CORE API endpoint for searching papers
        logger.info(f"searching core api for papers with topic: {topic}")
        entityType = "works"
        search_url = f"https://api.core.ac.uk/v3/search/{entityType}"

        headers = {
            "Authorization": f"Bearer {self.core_api_key}",
            "Content-Type": "application/json"
        }
        
        body = {
            "q": f"title:'{topic}' OR fullText:'{topic}'",
            "limit": 5,
            "filters": {
                "documentType": ["journal article", "conference paper", "review article", "preprint"],
                "language": ["en"]
            }
        }

        response = requests.post(search_url, headers=headers, json=body)
        response.raise_for_status()
        
        return self.parse_core_papers(response.json())
    
    # parse core api results
    def parse_core_papers(self, data: dict) -> list[dict]:
        logger.info("parsing core api results")
        results = []
        for item in data.get("results", []):

            title = item.get("title", "No title available")
            abstract = item.get("abstract")
            
            # if abstract is none summarize full text
            if not abstract and item.get("fullText"):
                abstract = self.summarize_core_papers(item.get("fullText"))

            # parse paper 
            paper = {
                "title": title,
                "type": item.get("documentType"),
                "summary": abstract,
                "pdfURL": item.get("downloadUrl")
            }

            results.append(paper)
        
        return results

    # summarize core api full text
    def summarize_core_papers(self, full_text: str) -> str:
        chunks = chunk_text_by_tokens(full_text)
        summary = summarize_chunks(chunks, self.llm_client)
        logger.info("summarized core api full text")
        logger.info(f"summary: {summary}")
        return summary
    
    def search_semantic_papers(self):
        pass

