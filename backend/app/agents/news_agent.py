# search news agents and return the latest news about the research topic
import logging

# initialize logging
logger = logging.getLogger(__name__)


class NewsAgent:
    def __init__(self, embedder):
        self.embedder = embedder

    def search_news(self, topic: str):
        pass


