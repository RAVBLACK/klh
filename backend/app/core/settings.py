"""
Application Settings
Core settings and configuration
"""

from pydantic_settings import BaseSettings
from typing import List


class AppSettings(BaseSettings):
    """Core application settings"""
    
    # Application
    PROJECT_NAME: str = "GST Filing Copilot API"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000"
    ]
    
    # Database
    DATABASE_URL: str = "sqlite:///./gst_copilot.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    class Config:
        env_file = ".env"
        case_sensitive = True


app_settings = AppSettings()
