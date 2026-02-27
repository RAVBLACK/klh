"""
GST Model
Data models for GST filing
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class GSTR1Entry(BaseModel):
    """GSTR-1 entry model"""
    gstin: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_date: Optional[datetime] = None
    taxable_value: Optional[float] = None
    igst: Optional[float] = None
    cgst: Optional[float] = None
    sgst: Optional[float] = None

class GSTR1Draft(BaseModel):
    """GSTR-1 draft model"""
    id: Optional[str] = None
    period: Optional[str] = None
    entries: Optional[List[GSTR1Entry]] = []
    created_at: Optional[datetime] = None
