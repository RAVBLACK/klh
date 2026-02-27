"""
AI Copilot - Explainer
Generate explanations for GST queries
"""

from typing import Dict


class CopilotExplainer:
    """Generate AI explanations for GST concepts"""
    
    def __init__(self):
        pass
    
    async def explain(self, query: str, context: Dict = None) -> str:
        """
        Generate explanation for user query
        """
        # Call LLM API with GST-specific prompts
        # For now, return placeholder
        
        explanations = {
            'gstin': 'GSTIN (Goods and Services Tax Identification Number) is a 15-digit unique code assigned to each taxpayer registered under GST.',
            'b2b': 'B2B (Business to Business) invoices are transactions between registered businesses where both parties have valid GSTIN.',
            'b2c': 'B2C (Business to Consumer) invoices are transactions where the buyer is an unregistered person or end consumer.'
        }
        
        query_lower = query.lower()
        for key, explanation in explanations.items():
            if key in query_lower:
                return explanation
        
        return 'I can help explain GST concepts. Try asking about GSTIN, B2B, B2C, or GSTR-1.'
    
    def suggest_corrections(self, invoice_data: Dict) -> List[str]:
        """Suggest corrections for invoice data"""
        suggestions = []
        
        if not invoice_data.get('gstin'):
            suggestions.append('Add GSTIN for B2B classification')
        
        if invoice_data.get('total_amount', 0) == 0:
            suggestions.append('Verify total amount')
        
        return suggestions
