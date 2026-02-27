"""
Invoice Model
Data models for invoice
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class InvoiceItem(BaseModel):
    """Invoice line item"""
    description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: Optional[float] = None

class Invoice(BaseModel):
    """Invoice data model"""
    id: Optional[str] = None
    invoice_number: Optional[str] = None
    date: Optional[datetime] = None
    vendor_name: Optional[str] = None
    gstin: Optional[str] = None
    total_amount: Optional[float] = None
    items: Optional[List[InvoiceItem]] = []
