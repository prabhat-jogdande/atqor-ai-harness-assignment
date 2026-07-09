import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
MODEL = SentenceTransformer("BAAI/bge-small-en-v1.5")


class ExampleRetriever:
    """
    Retrieves the most relevant few-shot examples
    using vector similarity search (FAISS).
    """

    def __init__(self):

        # Load few-shot examples
        with open("prompts/examples/examples.json", "r") as f:
            self.examples = json.load(f)

        # Extract only questions for embedding
        self.questions = [example["question"] for example in self.examples]

        # Generate normalized embeddings
        embeddings = MODEL.encode(
            self.questions,
            normalize_embeddings=True
        )

        # Create FAISS index using cosine similarity
        self.index = faiss.IndexFlatIP(embeddings.shape[1])

        # Add embeddings to index
        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve top-k semantically similar examples.
        """

        # Generate embedding for user query
        query_embedding = MODEL.encode(
            [query],
            normalize_embeddings=True
        )

        # Search similar examples
        scores, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        # Return matching examples
        return [
            self.examples[idx]
            for idx in indices[0]
        ]