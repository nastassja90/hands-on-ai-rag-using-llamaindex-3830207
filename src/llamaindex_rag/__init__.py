from .modules import ingestion, indexing
from .libs import Document, parse_config, Config
from os import getcwd, path
from typing import List
from nest_asyncio import apply


def __setup() -> Config:
    """Setup function to initialize the environment."""
    # Apply nest_asyncio to allow nested event loops
    apply()
    env_file: str = path.join(getcwd(), ".env")
    if not path.exists(env_file):
        raise FileNotFoundError(f".env file not found at {env_file}")
    return parse_config(env_file)


def main():

    config: Config = __setup()

    # add manual document
    additional_documents: List[Document] = [
        Document(
            text="This is a manually added document.",
            metadata={"source": "manual"},
        ),
    ]

    print(
        f"Loading documents from {config.directory} and transform them in BaseNodes..."
    )
    nodes = ingestion(config, additional_documents)


if __name__ == "__main__":
    main()
