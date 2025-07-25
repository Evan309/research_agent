import logging
import os
from dotenv import load_dotenv
from groq import Groq

# initialize env variables
load_dotenv()

# initialize logging
logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self, model: str = "llama3-70b-8192"):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model
        self.client = Groq(api_key=self.api_key)
        logger.info(f"initialized LLMClient with model: {self.model}")


    def generate_response(self, prompt: str, max_tokens: int, temperature: float = 0.7) -> str:

        # generate a response using the Groq client
        logger.info(f"sending prompt to Groq LLM API: {prompt}, with max tokens: {max_tokens}")

        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages = [{"role": "user", "content": prompt}],
                max_tokens = max_tokens,
                temperature = temperature
            )

            response = response.choices[0].message.content
            logger.info(f"Response generated: {response}")
            return response

        except Exception as e:
            logger.error(f"Groq LLM API call failed: {e}")
            return "Sorry, something went wrong generating the response."
