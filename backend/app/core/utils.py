import ast
from transformers import AutoTokenizer
from app.core.llm_client import LLMClient
from app.core.prompts import ARTICLE_SUMMARIZATION_PROMPT

tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-hf")

# splits a long text into chunks of at most "max tokens"
def chunk_text_by_tokens(text: str, max_tokens: int = 2000) -> list[str]:
    tokens = tokenizer.encode(text)
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)

    return chunks

# recursively summarize list of chunks
def summarize_chunks(chunks: list[str], llm: LLMClient, max_depth: int = 3, current_depth: int = 0) -> str:
    if not chunks:
        return ""
    
    # summarize each chunk
    summaries = []
    for chunk in chunks:
        prompt = ARTICLE_SUMMARIZATION_PROMPT.format(content=chunk)
        summary = llm.generate_response(prompt, 2500)
        summaries.append(summary)

    # combine to one summary
    combined_summary = "\n".join(summaries)

    # base case
    if len(summaries) == 1 or current_depth >= max_depth:
        return combined_summary.strip()
    
    # recursive call
    new_chunks = chunk_text_by_tokens(combined_summary)
    return summarize_chunks(new_chunks, llm, max_depth, current_depth + 1)

# parse list of subtasks from llm response
def extract_subtask_list(response: str) -> list[str]:
    try:
        # Find the line that starts with "Subtasks:"
        for line in response.splitlines():
            if line.strip().startswith("Subtasks:"):
                list_str = line.split("Subtasks:")[1].strip()
                return ast.literal_eval(list_str)
            
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing subtasks: {e}")
        return []