"""
Month Models
Pydantic models for month data
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class MonthBase(BaseModel):
    """Base month model"""
    month: str = Field(..., description="Month name (January, February, etc.)")
    shopId: str = Field(..., description="Associated shop ID")


class MonthCreate(MonthBase):
    """Month creation model"""
    pass


class MonthUpdate(BaseModel):
    """Month update model"""
    month: Optional[str] = None


class Month(MonthBase):
    """Full month model"""
    id: str
    createdAt: datetime
    invoiceCount: Optional[int] = 0
    
    class Config:
        from_attributes = True
