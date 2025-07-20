from typing import List
from enum import Enum

from llama_index.core.base.embeddings.base import (
    BaseEmbedding as LlamaBaseEmbedding,
    Embedding as LlamaEmbedding,
    SimilarityMode,
)

from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding


class EmbeddingModel(Enum):
    FASTEMBED = "BAAI/bge-large-en-v1.5-quantized"
    COHERE = "embed-english-v3.0"
    HUGGINGFACE = "BAAI/bge-small-en-v1.5"
    OPENAI = "text-embedding-3-small"


class Embedding:

    def __init__(
        self,
        model: EmbeddingModel = EmbeddingModel.FASTEMBED,
    ):
        self.__model: LlamaBaseEmbedding = FastEmbedEmbedding(model_name=model.value)
        if model == EmbeddingModel.COHERE:
            self.__model = CohereEmbedding(model_name=model.value)
        elif model == EmbeddingModel.HUGGINGFACE:
            self.__model = HuggingFaceEmbedding(model_name=model.value)
        elif model == EmbeddingModel.OPENAI:
            self.__model = OpenAIEmbedding(model_name=model.value)

    def get_text_embedding(self, text: str) -> list[float]:
        return self.__model.get_text_embedding(text)

    def get_embedding_dimensions(self, texts: List[str]) -> List[int]:
        embeddings: List[LlamaEmbedding] = self.__model.get_text_embedding_batch(texts)
        return [len(embedding) for embedding in embeddings]

    def similarity(self, text1: str, text2: str) -> float:
        return self.__model.similarity(
            embedding1=self.get_text_embedding(text1),
            embedding2=self.get_text_embedding(text2),
            mode=SimilarityMode.DEFAULT,
        )

    def model(self) -> LlamaBaseEmbedding:
        """Get the underlying LlamaBaseEmbedding model."""
        return self.__model
