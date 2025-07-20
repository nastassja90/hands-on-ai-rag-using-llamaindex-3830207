from typing import Any, Dict, Optional
from typing_extensions import Self
from llama_index.core import Document as LlamaDocument


class Document(LlamaDocument):
    """Custom Document class that extends LlamaIndex's Document."""

    def __init__(self, text: str, metadata: Optional[Dict[str, Any]] = None):
        self.__document: LlamaDocument = LlamaDocument(
            text=text, metadata=dict() if metadata is None else metadata
        )

    def upsert_metadata(self, metadata: Dict[str, Any]) -> Self:
        """upsert the document's metadata."""
        self.__document.metadata.update(metadata)
        return self

    def print(self) -> str:
        return f"{self.__document.__dict__}"

    def document(self) -> LlamaDocument:
        """Get the underlying LlamaDocument."""
        return self.__document
