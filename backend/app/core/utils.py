from transformers import AutoTokenizer
from app.core.llm_client import LLMClient
from app.core.prompts import ARTICLE_SUMMARIZATION_PROMPT

tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-hf")

# splits a long text into chunks of at most "max tokens"
def chunk_text_by_tokens(text: str, max_tokens: int = 3000) -> list[str]:
    tokens = tokenizer.encode(text)
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)

    return chunks

# recursively summarize list of chunks
def summarize_chunks(chunks: list[str], llm: LLMClient, max_tokens: int = 2000, max_depth: int = 3, current_depth: int = 0) -> str:
    
    if not chunks:
        return ""
    
    # summarize each chunk
    summaries = []
    for chunk in chunks:
        prompt = ARTICLE_SUMMARIZATION_PROMPT.format(content=chunk)
        