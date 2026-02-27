"""
GST Validator
Validate GST-related fields
"""

import re
from typing import Dict, List


class GSTValidator:
    """Validate GST invoice data"""
    
    def validate_gstin(self, gstin: str) -> Dict:
        """Validate GSTIN format and checksum"""
        if not gstin or len(gstin) != 15:
            return {'valid': False, 'error': 'Invalid GSTIN length'}
        
        pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
        
        if not re.match(pattern, gstin):
            return {'valid': False, 'error': 'Invalid GSTIN format'}
        
        return {'valid': True, 'error': None}
    
    def validate_invoice_data(self, data: Dict) -> Dict:
        """Validate complete invoice data"""
        errors = []
        warnings = []
        
        # Check required fields
        required_fields = ['invoice_number', 'date', 'gstin', 'total_amount']
        for field in required_fields:
            if not data.get(field):
                errors.append(f'Missing required field: {field}')
        
        # Validate GSTIN
        if data.get('gstin'):
            gstin_validation = self.validate_gstin(data['gstin'])
            if not gstin_validation['valid']:
                errors.append(gstin_validation['error'])
        
        # Validate amounts
        if data.get('total_amount', 0) < 0:
            errors.append('Total amount cannot be negative')
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
