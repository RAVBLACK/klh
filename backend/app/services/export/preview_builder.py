"""
Preview Builder
Build GSTR-1 preview data
"""

from typing import Dict, List


class PreviewBuilder:
    """Build GSTR-1 preview data for frontend"""
    
    def build_preview(self, gstr1_data: Dict) -> Dict:
        """
        Build comprehensive preview of GSTR-1 data
        """
        return {
            'month': gstr1_data.get('month'),
            'summary': self._build_summary(gstr1_data),
            'b2b': {
                'count': len(gstr1_data.get('b2b', [])),
                'total_value': self._sum_values(gstr1_data.get('b2b', [])),
                'invoices': gstr1_data.get('b2b', [])
            },
            'b2c_large': {
                'count': len(gstr1_data.get('b2c_large', [])),
                'total_value': self._sum_values(gstr1_data.get('b2c_large', [])),
                'invoices': gstr1_data.get('b2c_large', [])
            },
            'b2c_small': gstr1_data.get('b2c_small', {}),
            'totals': gstr1_data.get('totals', {})
        }
    
    def _build_summary(self, data: Dict) -> Dict:
        """Build summary statistics"""
        totals = data.get('totals', {})
        
        return {
            'total_invoices': (
                len(data.get('b2b', [])) +
                len(data.get('b2c_large', [])) +
                data.get('b2c_small', {}).get('count', 0)
            ),
            'total_taxable_value': totals.get('total_taxable_value', 0),
            'total_tax': totals.get('total_tax', 0),
            'total_igst': totals.get('total_igst', 0),
            'total_cgst': totals.get('total_cgst', 0),
            'total_sgst': totals.get('total_sgst', 0)
        }
    
    def _sum_values(self, invoices: List[Dict]) -> float:
        """Sum total values from invoices"""
        return sum(float(inv.get('value', 0)) for inv in invoices)
