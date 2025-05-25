"""
File: config.py
Description: This module defines the pydantic settings for the TextbookAI application.
Dependencies:
    - pydantic_settings
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"  # Default to SQLite
    
    class Config:
        env_file = ".env"

settings = Settings()

