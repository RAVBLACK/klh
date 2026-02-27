"""
LLM Client
Interface to Language Model for AI extraction
"""

from typing import Dict, List
import json


class LLMClient:
    """Client for interacting with LLM for invoice extraction"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # Initialize your LLM client (OpenAI, Anthropic, etc.)
    
    async def extract_invoice_data(self, ocr_text: str) -> Dict:
        """
        Use LLM to extract structured invoice data from OCR text
        """
        prompt = self._create_extraction_prompt(ocr_text)
        
        # Call LLM API
        # response = await self.llm.completion(prompt)
        
        # For now, return placeholder
        return {
            'invoice_number': '',
            'date': '',
            'gstin': '',
            'party_name': '',
            'items': [],
            'total_amount': 0,
            'cgst': 0,
            'sgst': 0,
            'igst': 0
        }
    
    def _create_extraction_prompt(self, ocr_text: str) -> str:
        """Create prompt for invoice extraction"""
        return f"""
Extract the following information from this invoice text:
- Invoice Number
- Date
- GSTIN
- Party Name
- Line Items (description, quantity, rate, amount)
- Tax amounts (CGST, SGST, IGST)
- Total Amount

OCR Text:
{ocr_text}

Return the data in JSON format.
"""
