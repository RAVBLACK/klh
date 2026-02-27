"""
Text Parser
Parse OCR text to extract invoice fields
"""

import re
from typing import Dict, Optional


class TextParser:
    """Parse OCR text to extract invoice data"""
    
    def __init__(self):
        self.patterns = {
            'gstin': r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}',
            'invoice_number': r'(?:Invoice|Bill|Receipt)[\s#:]*([A-Z0-9\-/]+)',
            'date': r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',
            'amount': r'₹?\s*(\d+(?:,\d{3})*(?:\.\d{2})?)',
        }
    
    def parse(self, text: str) -> Dict:
        """Parse text and extract invoice fields"""
        result = {
            'gstin': self.extract_gstin(text),
            'invoice_number': self.extract_invoice_number(text),
            'date': self.extract_date(text),
            'amount': self.extract_amount(text),
        }
        
        return result
    
    def extract_gstin(self, text: str) -> Optional[str]:
        """Extract GSTIN"""
        match = re.search(self.patterns['gstin'], text)
        return match.group(0) if match else None
    
    def extract_invoice_number(self, text: str) -> Optional[str]:
        """Extract invoice number"""
        match = re.search(self.patterns['invoice_number'], text, re.IGNORECASE)
        return match.group(1) if match else None
    
    def extract_date(self, text: str) -> Optional[str]:
        """Extract date"""
        match = re.search(self.patterns['date'], text)
        return match.group(0) if match else None
    
    def extract_amount(self, text: str) -> Optional[str]:
        """Extract total amount"""
        matches = re.findall(self.patterns['amount'], text)
        # Return the largest amount (likely total)
        if matches:
            amounts = [float(m.replace(',', '')) for m in matches]
            return str(max(amounts))
        return None
