"""
Shop Models
Pydantic models for shop data
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ShopBase(BaseModel):
    """Base shop model"""
    shopName: str = Field(..., min_length=1, max_length=200)
    shopType: str = Field(..., description="retail, wholesale, service, manufacturing")
    customerName: str = Field(..., min_length=1, max_length=200)


class ShopCreate(ShopBase):
    """Shop creation model"""
    pass


class ShopUpdate(BaseModel):
    """Shop update model"""
    shopName: Optional[str] = None
    shopType: Optional[str] = None
    customerName: Optional[str] = None


class Shop(ShopBase):
    """Full shop model"""
    id: str
    userId: str
    createdAt: datetime
    
    class Config:
        from_attributes = True
