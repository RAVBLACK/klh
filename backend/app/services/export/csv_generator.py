"""
CSV Generator
Generate CSV files for GSTR-1 export
"""

import csv
from typing import List, Dict
from io import StringIO


class CSVGenerator:
    """Generate GSTR-1 CSV files"""
    
    def generate_b2b_csv(self, invoices: List[Dict]) -> str:
        """Generate B2B invoices CSV"""
        output = StringIO()
        writer = csv.writer(output)
        
        # Header
        headers = [
            'GSTIN of Recipient', 'Invoice Number', 'Invoice Date',
            'Invoice Value', 'Place of Supply', 'Reverse Charge',
            'Invoice Type', 'E-Commerce GSTIN', 'Rate',
            'Taxable Value', 'Cess Amount'
        ]
        writer.writerow(headers)
        
        # Data rows
        for inv in invoices:
            row = [
                inv.get('gstin', ''),
                inv.get('invoice_number', ''),
                inv.get('date', ''),
                inv.get('total_amount', 0),
                inv.get('place_of_supply', ''),
                'N',
                'Regular',
                '',
                inv.get('tax_rate', 0),
                inv.get('taxable_value', 0),
                0
            ]
            writer.writerow(row)
        
        return output.getvalue()
    
    def generate_b2c_large_csv(self, invoices: List[Dict]) -> str:
        """Generate B2C Large invoices CSV"""
        output = StringIO()
        writer = csv.writer(output)
        
        headers = [
            'Invoice Number', 'Invoice Date', 'Invoice Value',
            'Place of Supply', 'Rate', 'Taxable Value', 'Cess Amount'
        ]
        writer.writerow(headers)
        
        for inv in invoices:
            row = [
                inv.get('invoice_number', ''),
                inv.get('date', ''),
                inv.get('total_amount', 0),
                inv.get('place_of_supply', ''),
                inv.get('tax_rate', 0),
                inv.get('taxable_value', 0),
                0
            ]
            writer.writerow(row)
        
        return output.getvalue()
