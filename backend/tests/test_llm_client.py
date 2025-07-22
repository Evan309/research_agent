import unittest
import backend.app.core.llm_client as llm_client
import os
import logging
from dotenv import load_dotenv

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestLLMClient(unittest.TestCase):
    def setUp(self):
        # Initialize the LLMClient with a mock API key and model
        self.client = llm_client.LLMClient(model="llama3-70b-8192")

    def test_generate_response(self):
        # Test the generate_response method with a sample prompt
        prompt = "What is the capital of France?"
        response = self.client.generate_response(prompt, max_tokens=50)

        logging.info(f"Response: {response}")
        
        # Check if the response is a string and not empty
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)


if __name__ == "__main__":
    unittest.main()