import sentence_transformers as st
import torch
import logging

#initialize logging
logger = logging.getLogger(__name__)

class EmbeddingClient:
    def __init__(self, model: str = "all-MiniLM-L6-v2"):
        self.model = st.SentenceTransformer(model)
        logger.info(f"intialized sentence transformer with model: {model}")

    def encode(self, text: str, to_tensor: bool = True):
        logger.info(f"embedding text: {text}, with convert_to_tensor set to {to_tensor}")
        return self.model.encode(text, convert_to_tensor=to_tensor)
    
    def similarity(self, emb_one, emb_two) -> torch.Tensor:
        logger.info(f"retrieving cos_sim between {emb_one} and {emb_two}")
        similarity = st.util.cos_sim(emb_one, emb_two)
        logger.info(f"similarity between {emb_one} and {emb_two}: {similarity.item()}")
        return similarity