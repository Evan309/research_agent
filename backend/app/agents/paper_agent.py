import logging
import os
import dotenv
import requests

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
    def __init__(self):
        self.core_api_key = os.getenv("CORE_API_KEY")

    # search papers through CORE API
    """ 
    core api internal server error
    implement later
    """
    def search_core_papers(self, topic: str, max_results: int = 10) -> list[dict]:
        # CORE API endpoint for searching papers
        entityType = "works"
        search_url = f"https://api.core.ac.uk/v3/search/works"

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
        
        return response.json()
    
    def search_semantic_papers(self):
        pass

