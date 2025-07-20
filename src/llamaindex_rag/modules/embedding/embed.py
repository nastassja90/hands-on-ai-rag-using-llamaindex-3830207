from . import Embedding, Config
from typing import List, Optional
from qdrant_client import QdrantClient
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.schema import BaseNode
from llama_index.vector_stores.qdrant import QdrantVectorStore


def indexing(config: Config, nodes: List[BaseNode]):
    client: Optional[QdrantClient] = None

    try:
        # initialize qdrant client
        client = QdrantClient(
            url=config.qdrant_url,
            api_key=config.qdrant_api_key,
        )

        embedding: Embedding = Embedding(model=config.embedding_model)

        vector_store = QdrantVectorStore(
            client=client,
            collection_name="it_can_be_done",
            embed_model=embedding.model(),
        )

        # assign qdrant vector store to storage context
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store,
        )
        # create the index from the nodes
        index: VectorStoreIndex = VectorStoreIndex(
            nodes,
            embed_model=embedding.model(),
            show_progress=True,
            storage_context=storage_context,
        )

    except Exception as e:
        print(f"An error occurred during indexing: {e}")
        raise e
    finally:
        if client:
            client.close()
