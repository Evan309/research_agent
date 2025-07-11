import logging
import requests
from readability import Document
from bs4 import BeautifulSoup

# initialize logging
logger = logging.getLogger(__name__)

class WebScraperClient:
    def __init__(self, user_agent: str = "Mozilla/5.0"):
        self.headers = {"User-agent": user_agent}

    # scrapes main content of the article url for llm to summarize
    def scrape_article_url(self, url: str) -> str:
        try: 
            logger.info(f"trying to scrape url: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            doc = Document(response.text)
            title = doc.short_title()

            summary_html = doc.summary()
            soup = BeautifulSoup(summary_html, "html.parser")
            paragraphs = soup.find_all("p")

            # Join all paragraphs — full article text
            content = " ".join(p.get_text() for p in paragraphs)

            return {
                "url": url,
                "title": title.strip(),
                "content": content.strip()
            }

        except Exception as e:
            return {
                "url": url,
                "error": str(e)
            } 
        