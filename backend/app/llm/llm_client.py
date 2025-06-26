# use groq with llama3-70b-8192
import logging
from groq import Groq

# initialize logging
logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self, api_key: str, model: str = "llama3-70b-8192"):
        self.api_key = api_key
        self.model = model
        self.client = Groq(api_key=api_key)
        logger.info(f"initialized LLMClient with model: {self.model}")


    def generate_response(self, prompt: str, max_tokens: int, temperature: float = 0.7) -> str:

        # gerate a response using the Groq client
        logger.info(f"Generating response for prompt: {prompt} with max_tokens: {max_tokens}")
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "user", "content": prompt}],
            max_tokens = max_tokens,
            temperature = temperature
        )

        logger.info(f"Response generated: {response.choices[0].message.content}")
        return response.choices[0].message.content
