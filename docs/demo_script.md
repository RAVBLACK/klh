# Demo Script

## GST Filing Copilot - Product Demo

### Duration: 10 minutes

---

## Introduction (1 min)

**Problem Statement:**
Small and medium businesses struggle with GST filing due to:
- Manual data entry from paper invoices
- High error rates in data extraction
- Complex GST calculation and filing process
- Lack of real-time guidance

**Solution:**
GST Filing Copilot - An AI-powered mobile app that:
- Captures invoices via camera
- Extracts data using AI
- Generates GSTR-1 drafts automatically
- Provides intelligent copilot assistance

---

## Demo Flow

### 1. User Registration & Login (1 min)

**Actions:**
1. Open the app on mobile device
2. Click "Sign Up"
3. Enter:
   - Email: demo@gstcopilot.com
   - Password: ••••••••
   - Business Name: ABC Enterprises
   - GSTIN: 27XXXXX1234X1Z5
4. Click "Register"
5. Navigate to Dashboard

**Key Points:**
- Simple, mobile-first interface
- Secure Firebase authentication
- Business details captured upfront

---

### 2. Invoice Capture & Upload (2 min)

**Actions:**
1. Click "Upload Invoice" from Dashboard
2. Grant camera permission
3. Capture invoice image (or upload from gallery)
4. Show image preview
5. Click "Process"
6. Wait for processing animation

**Key Points:**
- Native camera integration
- Works offline (captures locally)
- Real-time image preview
- Background processing

---

### 3. View Extracted Data (2 min)

**Actions:**
1. Show extracted invoice details:
   - Invoice Number: INV-2024-001
   - Date: 10 Jan 2024
   - Vendor: XYZ Suppliers
   - Vendor GSTIN: 27YYYYY5678Y1Z9
   - Items:
     * Product A: ₹10,000
     * GST @ 18%: ₹1,800
   - Total: ₹11,800
   - Confidence Score: 87%

2. Highlight confidence badges:
   - Green (>85%): High confidence
   - Yellow (70-85%): Medium confidence
   - Red (<70%): Manual review needed

3. Allow user to edit any field
4. Click "Verify & Save"

**Key Points:**
- Accurate AI extraction
- Confidence scoring for transparency
- Manual edit capability
- Validation before saving

---

### 4. AI Copilot Assistance (2 min)

**Actions:**
1. Click on Copilot icon (bottom nav)
2. Demo chat interactions:

   **User:** "Is this GSTIN valid?"
   **Copilot:** "Yes, the GSTIN 27YYYYY5678Y1Z9 follows the correct format for Maharashtra state."

   **User:** "What's the GST rate for electronics?"
   **Copilot:** "GST rate for most electronics is 18%. However, specific items may have different rates. Would you like me to check a specific product?"

   **User:** "Can I claim ITC on this invoice?"
   **Copilot:** "Based on the invoice details, you can claim Input Tax Credit (ITC) if: 1) The supplier GSTIN is valid, 2) You've received the goods/services, and 3) The invoice follows GST rules. I recommend verifying the supplier GSTIN on the GST portal."

3. Show suggestions panel with quick actions

**Key Points:**
- Context-aware AI assistant
- Natural language queries
- Actionable suggestions
- Educational guidance

---

### 5. Generate GSTR-1 (1.5 min)

**Actions:**
1. Navigate to "GST Filing" section
2. Select tax period: January 2024
3. Show list of verified invoices
4. Select invoices to include
5. Click "Generate GSTR-1"
6. Show draft generation progress
7. Display GSTR-1 preview:
   - B2B supplies section
   - Invoice-wise details
   - Tax calculations:
     * Total Taxable Value: ₹50,000
     * IGST: ₹9,000
     * CGST: ₹0
     * SGST: ₹0

**Key Points:**
- Auto-compilation from invoices
- Period-wise organization
- Standard GSTR-1 format
- Automatic tax calculations

---

### 6. Review & Export (1.5 min)

**Actions:**
1. Review GSTR-1 draft line by line
2. Ask Copilot: "Is this ready to file?"
3. Copilot reviews and provides checklist:
   - ✓ All invoices verified
   - ✓ GSTIN validations passed
   - ✓ Tax calculations correct
   - ⚠ Recommendation: Verify supplier GSTINs on portal

4. Click "Export"
5. Choose format: Excel
6. Download file
7. Show downloaded Excel (GSTR-1 format)

**Key Points:**
- Pre-filing validation
- Multiple export formats (JSON, Excel, CSV)
- Ready for GST portal upload
- Audit trail maintained

---

### 7. Dashboard Overview (30 sec)

**Actions:**
1. Return to Dashboard
2. Show key metrics:
   - Total Invoices: 15
   - This Month: ₹1,50,000
   - GST to Pay: ₹27,000
   - Pending Verification: 2
3. Show recent activity timeline

**Key Points:**
- At-a-glance overview
- Visual analytics
- Actionable insights
- Activity tracking

---

## Closing (30 sec)

**Key Benefits:**
- ⚡ **90% faster** data entry
- ✓ **High accuracy** with AI extraction
- 🤖 **24/7 copilot** assistance
- 📱 **Mobile-first** design
- 🔒 **Secure** with Firebase

**Disclaimer:**
This tool generates DRAFT GST returns only. Users should review all data before filing with the GST portal. Always consult a tax professional for compliance.

**Call to Action:**
- Sign up for early access
- Try the demo at: gstcopilot.com/demo
- Contact: support@gstcopilot.com

---

## Backup Scenarios

### If Camera Fails:
- Use pre-loaded sample invoices
- Upload from gallery

### If Processing is Slow:
- Explain: "Real-world processing takes 5-10 seconds"
- Show processing indicators
- Highlight background processing capability

### If Extraction Accuracy is Low:
- Show manual edit capability
- Explain confidence scoring system
- Demonstrate learning from corrections

---

## Q&A Preparation

**Q: What if the invoice is unclear?**
A: The system shows low confidence scores and allows manual entry. Over time, the AI learns and improves.

**Q: Does it support multiple languages?**
A: Currently English. Regional languages coming soon.

**Q: Is my data secure?**
A: Yes, we use Firebase with bank-grade security. Your data is encrypted and isolated.

**Q: Can I use this for filing?**
A: This generates drafts. You must review and upload to the official GST portal.

**Q: What's the pricing?**
A: [Mention pricing tiers if available]

**Q: How accurate is the AI?**
A: 85-95% accuracy depending on invoice quality. All extractions are verified by users.
