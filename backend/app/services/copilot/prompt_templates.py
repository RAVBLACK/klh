"""
Copilot Prompt Templates
Predefined prompts for AI copilot
"""


INVOICE_EXTRACTION_PROMPT = """
You are an expert at extracting structured data from Indian GST invoices.

Extract the following information from the invoice text:
1. Invoice Number
2. Invoice Date
3. Supplier GSTIN
4. Buyer GSTIN (if available)
5. Party/Customer Name
6. Line Items with:
   - Description
   - HSN/SAC Code
   - Quantity
   - Unit Price
   - Amount
7. Tax Breakdown:
   - Taxable Value
   - CGST (%)
   - SGST (%)
   - IGST (%)
   - CGST Amount
   - SGST Amount
   - IGST Amount
8. Total Invoice Value

Return the data in JSON format.
"""


GST_EXPLANATION_PROMPT = """
You are a helpful GST filing assistant for Indian businesses.
Explain GST concepts in simple terms.

User Question: {question}

Provide a clear, concise explanation focusing on:
- Definition
- When it applies
- How it affects filing
- Any important rules or limits
"""


INVOICE_VALIDATION_PROMPT = """
Review this invoice data for GST compliance:

{invoice_data}

Check for:
1. Valid GSTIN format
2. Mandatory fields present
3. Tax calculations correct
4. Appropriate classification (B2B/B2C)

Return validation result with any errors or warnings.
"""
