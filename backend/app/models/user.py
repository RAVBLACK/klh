"""
User Model
Data models for user
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    """User data model"""
    id: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    business_name: Optional[str] = None
    gstin: Optional[str] = None
    created_at: Optional[datetime] = None
