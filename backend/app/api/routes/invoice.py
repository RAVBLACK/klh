"""
Invoice Routes
Handle invoice processing endpoints
"""

from fastapi import APIRouter

router = APIRouter(prefix="/invoice", tags=["invoice"])

@router.post("/upload")
def upload_invoice():
    """Upload and process invoice image"""
    pass

@router.get("/{invoice_id}")
def get_invoice(invoice_id: str):
    """Get invoice details"""
    pass

@router.get("/")
def list_invoices():
    """List all invoices"""
    pass
