"""
GST Classifier
Classify invoices for GSTR-1 tables
"""

from typing import Dict


class GSTClassifier:
    """Classify invoices into GST return categories"""
    
    def classify(self, invoice_data: Dict) -> str:
        """
        Classify invoice into GSTR-1 table
        - B2B: Business to Business
        - B2C Large: B2C invoices > 2.5 lakhs
        - B2C Small: B2C invoices < 2.5 lakhs
        - Exports
        - Nil Rated / Exempted
        """
        amount = float(invoice_data.get('total_amount', 0))
        gstin = invoice_data.get('gstin', '')
        
        # Has GSTIN = B2B
        if gstin and len(gstin) == 15:
            return 'B2B'
        
        # No GSTIN, check amount
        if amount > 250000:
            return 'B2C_LARGE'
        else:
            return 'B2C_SMALL'
    
    def get_table_name(self, classification: str) -> str:
        """Get GSTR-1 table name for classification"""
        mapping = {
            'B2B': '4A, 4B, 4C, 6B, 6C',
            'B2C_LARGE': '5A, 5B',
            'B2C_SMALL': '7',
            'EXPORT': '6A',
            'NIL_RATED': '8'
        }
        return mapping.get(classification, '7')
