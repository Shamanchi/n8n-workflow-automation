from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    n8n_url: str = 'http://localhost:5678'
    n8n_api_key: Optional[str] = None
    database_url: str = 'sqlite:///./workflows.db'
    rss_feeds: List[str] = []
    telegram_bot_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()