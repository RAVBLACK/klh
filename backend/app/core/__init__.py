"""
Core Configuration
Application core configuration
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    environment: str = "development"
    firebase_credentials: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
