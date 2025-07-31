from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from app.agents.task_planner import TaskPlanner
from app.agents.dataset_agent import DatasetAgent
from app.agents.news_agent import NewsAgent
from app.agents.paper_agent import PaperAgent
from app.agents.summarizer import Summarizer
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
summarizer = Summarizer(llm_client=llm_client)

# POST route for query
@app.post("/query")
async def query_endpoint(request: QueryRequest):
    logger.info(f"Received query: {request.query}")

    results = {
        "topic": None,
        "intent": None,
        "response": None,
        "research_results": None
    }

    # classify intent and topic
    topic = task_planner.get_topic(request.query)
    logger.info(f"prompt topic: {topic}")
    intent = task_planner.classify_intent(request.query)
    results["intent"] = intent
    logger.info(f"prompt intent: {intent}")

    if intent == "chat":
        # generate chat response
        logger.info("generating chat response")
        chat_response = llm_client.generate_response(request.query, 500)
        logger.info(f"response: {chat_response}")
        results["response"] = chat_response

    elif intent == "research":
        research_results = {
            "datasets": None,
            "papers": None,
            "news": None
        }

        # get subtasks
        subtasks = task_planner.get_subtasks(request.query)
        
        # execute subtasks
        if "find_datasets" in subtasks:
            research_results["datasets"] = dataset_agent.search_kaggle_datasets(topic, 3)
        if "find_news" in subtasks:
            research_results["news"] = news_agent.search_GNEWS(topic, 3)
        if "find_papers" in subtasks:
            research_results["papers"] = paper_agent.search_core_papers(topic, 3)

        # summarize response
        research_results["response"] = summarizer.summarize(research_results, request.query)
        results["research_results"] = research_results

    return results