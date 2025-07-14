import unittest
import logging
from app.core.utils import chunk_text_by_tokens

# initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestUtils(unittest.TestCase):
    def test_chunk_text_by_tokens(self):
        