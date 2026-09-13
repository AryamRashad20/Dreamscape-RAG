from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dreamscape RAG API"
    VERSION: str = "1.0.0"

    VECTOR_STORE_DIR: Path = PROJECT_ROOT / "data" / "vector_store"
    INDEX_PATH: Path = VECTOR_STORE_DIR / "dreamscape.index"
    METADATA_PATH: Path = VECTOR_STORE_DIR / "metadata.json"
    CONFIG_PATH: Path = VECTOR_STORE_DIR / "config.json"

    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"

    OLLAMA_MODEL: str = "llama3.2:3b"
    TOP_K: int = 3

    API_PREFIX: str = "/api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()