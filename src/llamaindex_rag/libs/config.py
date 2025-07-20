from .embedding import EmbeddingModel
from dataclasses import dataclass
from dotenv import load_dotenv
from os import environ, path, getcwd


@dataclass
class Config:
    """Configuration class for the application."""

    directory: str
    embedding_model: EmbeddingModel
    cohere_api_key: str
    qdrant_api_key: str
    qdrant_url: str
    openai_api_key: str


def parse_config(env: str) -> Config:
    """Parse a Config object from a .env file."""
    # Load environment variables from .env file
    load_dotenv(dotenv_path=env)

    return Config(
        directory=path.join(getcwd(), "data"),
        embedding_model=EmbeddingModel[
            environ.get("EMBEDDING_MODEL", EmbeddingModel.FASTEMBED.name)
        ],
        cohere_api_key=environ.get("CO_API_KEY", ""),
        qdrant_api_key=environ.get("QDRANT_API_KEY", ""),
        qdrant_url=environ.get("QDRANT_URL", ""),
        openai_api_key=environ.get("OPENAI_API_KEY", ""),
    )
