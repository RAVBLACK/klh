"""
AI Extractor
Coordinate AI-powered invoice data extraction
"""

from typing import Dict
from app.services.ai_extraction.llm_client import LLMClient


class AIExtractor:
    """Extract invoice data using AI"""
    
    def __init__(self):
        self.llm_client = LLMClient()
    
    async def extract(self, ocr_data: Dict) -> Dict:
        """
        Extract structured invoice data from OCR results
        """
        raw_text = ocr_data.get('raw_text', '')
        
        # Use LLM to extract structured data
        extracted_data = await self.llm_client.extract_invoice_data(raw_text)
        
        # Add confidence scores
        extracted_data['confidence_scores'] = self._calculate_confidence(
            extracted_data, ocr_data
        )
        
        return extracted_data
    
    def _calculate_confidence(self, extracted: Dict, ocr: Dict) -> Dict:
        """Calculate confidence scores for extracted fields"""
        # Implement confidence calculation logic
        return {
            'overall': 0.85,
            'invoice_number': 0.90,
            'date': 0.88,
            'gstin': 0.92,
            'amount': 0.87
        }
