# GST Logic Notes

## GSTR-1 Overview

GSTR-1 is a monthly/quarterly return that contains details of outward supplies of goods and services.

## Invoice Classification

### B2B (Business to Business)
- **Tables**: 4A, 4B, 4C, 6B, 6C
- **Criteria**: Both parties have valid GSTIN
- **Requirements**:
  - Supplier GSTIN
  - Recipient GSTIN
  - Invoice Number
  - Invoice Date
  - Invoice Value
  - Taxable Value
  - Tax amounts (CGST, SGST, IGST)

### B2C Large (Invoice > ₹2.5 Lakhs)
- **Tables**: 5A, 5B
- **Criteria**: 
  - No GSTIN of recipient
  - Invoice value > ₹2,50,000
- **Requirements**:
  - Invoice Number
  - Invoice Date
  - Invoice Value
  - Place of Supply
  - Tax Rate

### B2C Small (Invoice ≤ ₹2.5 Lakhs)
- **Table**: 7
- **Criteria**: 
  - No GSTIN of recipient
  - Invoice value ≤ ₹2,50,000
- **Requirements**:
  - Aggregated data by rate and place of supply
  - No individual invoice details needed

### Exports
- **Table**: 6A
- **Criteria**: Goods/Services exported
- **Types**:
  - With payment of tax
  - Without payment of tax (under bond/LUT)

### Nil Rated / Exempted
- **Table**: 8
- **Supplies**: Nil rated, exempted, or non-GST supplies

## Tax Calculation

### Intra-State Supply
- **CGST**: Central GST (e.g., 9%)
- **SGST**: State GST (e.g., 9%)
- **Total**: CGST + SGST = 18%

### Inter-State Supply
- **IGST**: Integrated GST (e.g., 18%)
- Applied when supplier and recipient are in different states

## GSTIN Format

**15 Characters**: `22AAAAA0000A1Z5`

1. **Characters 1-2**: State Code (22 = Chhattisgarh)
2. **Characters 3-12**: PAN of taxpayer
3. **Character 13**: Entity Code
4. **Character 14**: Blank (default 'Z')
5. **Character 15**: Check digit

## Validation Rules

1. **GSTIN**: Must be 15 characters, valid format
2. **Invoice Number**: Mandatory, alphanumeric
3. **Date**: Valid date format (DD/MM/YYYY or DD-MM-YYYY)
4. **Amount**: Must be positive number
5. **Tax Rates**: Standard rates - 0%, 5%, 12%, 18%, 28%

## Common Issues

1. **Missing GSTIN**: Cannot classify as B2B
2. **Invalid Date Format**: Parsing errors
3. **Incorrect Tax Calculation**: CGST + SGST ≠ Total Tax
4. **Duplicate Invoice Numbers**: Same invoice uploaded twice

## Filing Frequency

- **Monthly**: Businesses with turnover > ₹5 Crores
- **Quarterly**: Businesses with turnover ≤ ₹5 Crores (QRMP scheme)

## Due Dates

- **Monthly**: 11th of next month
- **Quarterly**: 13th of month following quarter
