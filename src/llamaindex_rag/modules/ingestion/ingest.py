from . import Document, Config
from typing import List
from llama_index.core import SimpleDirectoryReader
from llama_index.core.schema import BaseNode
from llama_index.core.node_parser import SentenceSplitter


def __transform(documents: List[Document]) -> List[BaseNode]:

    parser = SentenceSplitter(
        chunk_size=128,  # in tokens
        chunk_overlap=16,  # in tokens
        paragraph_separator="\n\n",
    )

    llama_documents = [doc.document() for doc in documents]
    return parser.get_nodes_from_documents(llama_documents, show_progress=True)


def __load(directory: str) -> List[Document]:
    documents: List[Document] = list()
    for doc in SimpleDirectoryReader(directory).load_data():
        documents.append(Document(text=doc.text, metadata=doc.metadata))
    return documents


def ingestion(config: Config, additional_documents: List[Document]) -> List[BaseNode]:
    documents = __load(config.directory)
    documents.extend(additional_documents)
    return __transform(documents)
