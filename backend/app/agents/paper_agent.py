import logging
import os
import dotenv
import requests

# initialize logging
logger = logging.getLogger(__name__)

# load environment variables
dotenv.load_dotenv()

class PaperAgent:
    def __init__(self):
        self.core_api_key = os.getenv("CORE_API_KEY")

    # search papers through CORE API
    def search_core_papers(self, topic: str, max_results: int = 10) -> list[dict]:
        # CORE API endpoint for searching papers
        entityType = "outputs"
        search_url = f"https://api.core.ac.uk/v3/search/{entityType}"
        headers = {"Authorization": f"Bearer {self.core_api_key}"}
        body = {
            "q": f"title:'{topic}' OR fullText:'{topic}'",
            "limit": max_results,
            "filters": {
                "language": ["en"],
                "documentType": ["research", 
                                 "research article", 
                                 "conference paper"]
            }, 
            "sort": [
                {
                    "field": "yearPublished",
                    "order": "desc"
                }
            ]
        }

        response = requests.post(search_url, headers=headers, json=body)
        response.raise_for_status()
        
        return response.json()

