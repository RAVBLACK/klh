"""
GSTR-1 Mapper
Map invoice data to GSTR-1 format
"""

from typing import Dict, List


class GSTR1Mapper:
    """Map invoice data to GSTR-1 return format"""
    
    def map_to_gstr1(self, invoices: List[Dict], month: str) -> Dict:
        """
        Map list of invoices to GSTR-1 format
        """
        from app.services.gst_logic.classifier import GSTClassifier
        
        classifier = GSTClassifier()
        
        # Group invoices by classification
        b2b_invoices = []
        b2c_large = []
        b2c_small = []
        
        for invoice in invoices:
            classification = classifier.classify(invoice)
            
            if classification == 'B2B':
                b2b_invoices.append(invoice)
            elif classification == 'B2C_LARGE':
                b2c_large.append(invoice)
            else:
                b2c_small.append(invoice)
        
        # Calculate totals
        totals = self._calculate_totals(invoices)
        
        return {
            'month': month,
            'b2b': self._format_b2b(b2b_invoices),
            'b2c_large': self._format_b2c_large(b2c_large),
            'b2c_small': self._format_b2c_small(b2c_small),
            'totals': totals
        }
    
    def _format_b2b(self, invoices: List[Dict]) -> List[Dict]:
        """Format B2B invoices"""
        return [
            {
                'gstin': inv.get('gstin'),
                'invoice_number': inv.get('invoice_number'),
                'date': inv.get('date'),
                'value': inv.get('total_amount'),
                'taxable_value': inv.get('taxable_value'),
                'igst': inv.get('igst', 0),
                'cgst': inv.get('cgst', 0),
                'sgst': inv.get('sgst', 0)
            }
            for inv in invoices
        ]
    
    def _format_b2c_large(self, invoices: List[Dict]) -> List[Dict]:
        """Format B2C Large invoices"""
        return invoices
    
    def _format_b2c_small(self, invoices: List[Dict]) -> Dict:
        """Format B2C Small (aggregated)"""
        total = sum(float(inv.get('total_amount', 0)) for inv in invoices)
        count = len(invoices)
        
        return {
            'count': count,
            'total_value': total
        }
    
    def _calculate_totals(self, invoices: List[Dict]) -> Dict:
        """Calculate total values"""
        total_taxable = sum(float(inv.get('taxable_value', 0)) for inv in invoices)
        total_igst = sum(float(inv.get('igst', 0)) for inv in invoices)
        total_cgst = sum(float(inv.get('cgst', 0)) for inv in invoices)
        total_sgst = sum(float(inv.get('sgst', 0)) for inv in invoices)
        
        return {
            'total_taxable_value': total_taxable,
            'total_igst': total_igst,
            'total_cgst': total_cgst,
            'total_sgst': total_sgst,
            'total_tax': total_igst + total_cgst + total_sgst
        }
