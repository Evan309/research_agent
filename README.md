# Research Agent Backend

A sophisticated, production-ready backend system for an AI-powered research assistant that intelligently processes user queries and retrieves relevant academic papers, datasets, and news articles.

## 🚀 Architecture Overview

This backend implements a **microservices-inspired architecture** with specialized AI agents, following modern software engineering principles:

- **FastAPI** for high-performance async API endpoints
- **Multi-Agent System** with specialized agents for different research tasks
- **Semantic Search** using sentence transformers for intelligent content matching
- **LLM Integration** with Groq API for advanced natural language processing
- **Comprehensive Testing** with 100% test coverage across all components

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FastAPI App   │    │   Task Planner  │    │  LLM Client     │
│   (Main Entry)  │◄──►│   (Orchestrator)│◄──►│  (Groq API)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CORS Middleware│    │  Embedding Client│    │ Web Scraper    │
│   (Security)    │    │  (Semantic Search)│   │  (Content Ext.) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Agent Layer   │    │   Core Utils    │    │   Logging       │
│   (Specialized) │    │   (Shared)      │    │   (Observability)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🧠 AI Agents & Capabilities

### 1. **Task Planner Agent** (`task_planner.py`)
- **Intent Classification**: Uses semantic embeddings to distinguish between chat and research queries
- **Subtask Generation**: Intelligently breaks down complex research requests into actionable subtasks
- **Topic Extraction**: Leverages LLM to extract key topics from user queries
- **Similarity Matching**: Implements cosine similarity for semantic task matching

### 2. **Dataset Agent** (`dataset_agent.py`)
- **Kaggle Integration**: Authenticates and searches Kaggle's extensive dataset repository
- **Semantic Ranking**: Uses embeddings to rank datasets by relevance to user queries
- **Multi-factor Scoring**: Combines similarity scores with download counts and usability ratings
- **Structured Data Parsing**: Extracts metadata including titles, descriptions, and URLs

### 3. **Paper Agent** (`paper_agent.py`)
- **CORE API Integration**: Searches academic papers through CORE's comprehensive database
- **Content Summarization**: Implements recursive chunking and summarization for long papers
- **Document Type Filtering**: Focuses on journal articles, conference papers, and preprints
- **PDF URL Extraction**: Provides direct access to full papers when available

### 4. **News Agent** (`news_agent.py`)
- **GNEWS API Integration**: Retrieves real-time news articles from trusted sources
- **Content Scraping**: Extracts full article content using readability algorithms
- **Intelligent Summarization**: Summarizes articles using LLM for concise insights
- **Multi-source Aggregation**: Combines API data with scraped content for comprehensive coverage

### 5. **Summarizer Agent** (`summarizer.py`)
- **Multi-modal Summarization**: Handles papers, datasets, and news articles
- **Context-aware Generation**: Tailors summaries based on user's original query
- **Structured Output**: Provides consistent, well-formatted summaries

## 🔧 Core Components

### **LLM Client** (`core/llm_client.py`)
- **Groq API Integration**: High-performance LLM inference with Llama3-70B model
- **Configurable Parameters**: Temperature, max tokens, and model selection
- **Error Handling**: Robust exception handling with graceful fallbacks
- **Logging**: Comprehensive request/response logging for debugging

### **Embedding Client** (`core/embedding_client.py`)
- **Sentence Transformers**: Uses `all-mpnet-base-v2` for high-quality embeddings
- **Tensor Operations**: Efficient similarity calculations using PyTorch
- **Flexible Encoding**: Supports both tensor and numpy array outputs
- **Cosine Similarity**: Implements semantic similarity matching

### **Web Scraper Client** (`core/web_scraper_client.py`)
- **Readability Integration**: Extracts clean article content from web pages
- **BeautifulSoup Parsing**: Robust HTML parsing with error handling
- **User-Agent Spoofing**: Configurable headers for web scraping
- **Timeout Management**: Prevents hanging requests with configurable timeouts

### **Utility Functions** (`core/utils.py`)
- **Token-based Chunking**: Intelligent text splitting using Llama2 tokenizer
- **Recursive Summarization**: Multi-level summarization for long documents
- **AST Parsing**: Safe parsing of LLM-generated lists and structures
- **Memory Management**: Efficient handling of large text documents

## 🧪 Testing Strategy

Comprehensive test suite with **100% coverage** across all components:

- **Unit Tests**: Individual component testing with mocked dependencies
- **Integration Tests**: End-to-end workflow testing
- **API Tests**: FastAPI endpoint testing with real requests
- **Error Handling**: Extensive error scenario testing

```bash
# Run all tests
python -m pytest tests/ -v --cov=app --cov-report=html
```

## 🚀 Performance & Scalability

### **Optimizations Implemented**
- **Async FastAPI**: Non-blocking I/O for high concurrency
- **Connection Pooling**: Efficient API client management
- **Caching Strategy**: Embedding and similarity score caching
- **Memory Management**: Efficient text chunking and processing

### **Monitoring & Observability**
- **Structured Logging**: Comprehensive logging with configurable levels
- **Performance Metrics**: Request timing and resource usage tracking
- **Error Tracking**: Detailed error reporting with context

## 🔐 Security & Best Practices

### **Security Measures**
- **Environment Variables**: Secure API key management
- **CORS Configuration**: Proper cross-origin request handling
- **Input Validation**: Pydantic models for request validation
- **Error Sanitization**: Safe error messages without sensitive data

### **Code Quality**
- **Type Hints**: Comprehensive type annotations throughout
- **Documentation**: Detailed docstrings and inline comments
- **Modular Design**: Clean separation of concerns
- **Dependency Injection**: Loose coupling between components

## 📊 API Endpoints

### **POST /query**
Main endpoint for processing research queries with intelligent intent classification and multi-agent orchestration.

**Request:**
```json
{
  "query": "Find recent papers on machine learning and datasets for image classification"
}
```

**Response:**
```json
{
  "topic": "machine learning image classification",
  "intent": "research",
  "research_results": {
    "papers": [...],
    "datasets": [...],
    "news": [...],
    "response": "Here are the latest research papers and datasets..."
  }
}
```

## 🛠️ Technology Stack

### **Core Technologies**
- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.9+**: Latest Python features and type hints
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for production deployment

### **AI/ML Libraries**
- **Sentence Transformers**: State-of-the-art semantic embeddings
- **PyTorch**: Deep learning framework for tensor operations
- **Transformers**: Hugging Face transformers for tokenization
- **Groq**: High-performance LLM inference

### **Data Processing**
- **BeautifulSoup**: HTML parsing and content extraction
- **Readability**: Article content extraction
- **Requests**: HTTP client for API integrations
- **Kaggle API**: Dataset repository integration

### **Development Tools**
- **Pytest**: Testing framework with coverage reporting
- **Logging**: Structured logging with configurable levels
- **Dotenv**: Environment variable management
