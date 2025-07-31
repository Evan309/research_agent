from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from app.agents.task_planner import TaskPlanner
from app.agents.dataset_agent import DatasetAgent
from app.agents.news_agent import NewsAgent
from app.agents.paper_agent import PaperAgent
from app.core.embedding_client import EmbeddingClient
from app.core.llm_client import LLMClient
from app.core.web_scraper_client import WebScraperClient

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup FastAPI
app = FastAPI()

# Allow frontend connection (React localhost for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or "*" for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request
class QueryRequest(BaseModel):
    query: str

# Load core services
embedder = EmbeddingClient()
llm_client = LLMClient()
web_scraper = WebScraperClient()

# Load agents
task_planner = TaskPlanner(embedder=EmbeddingClient, LLM_client=llm_client)
dataset_agent = DatasetAgent(embedder=embedder)
news_agent = NewsAgent(embedder=EmbeddingClient, web_scraper=web_scraper, LLM_client=llm_client)
paper_agent = PaperAgent(LLM_client=llm_client)