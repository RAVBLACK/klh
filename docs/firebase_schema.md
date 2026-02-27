# Firebase Schema Documentation

## Collections Overview

The application uses four main Firestore collections to store data:

1. **users** - User profiles and business information
2. **invoices** - Invoice data extracted from images
3. **gstr1_drafts** - Generated GSTR-1 draft returns
4. **copilot_chats** - AI copilot chat sessions

---

## Collection: `users`

Stores user profile and business information.

### Document Structure
```javascript
{
  uid: string,                    // Firebase Auth user ID (primary key)
  email: string,                  // User email address
  name: string,                   // User full name
  businessName: string,           // Business name (optional)
  gstin: string,                  // Business GSTIN number (optional)
  phone: string,                  // Contact phone number (optional)
  createdAt: Timestamp,           // Account creation timestamp
  updatedAt: Timestamp            // Last update timestamp
}
```

### Example Document
```json
{
  "uid": "abc123xyz",
  "email": "john@example.com",
  "name": "John Doe",
  "businessName": "ABC Corporation",
  "gstin": "27XXXXX1234X1Z5",
  "phone": "+91 9876543210",
  "createdAt": "2024-01-15T10:00:00Z",
  "updatedAt": "2024-01-15T10:00:00Z"
}
```

### Indexes
- `uid` (automatic document ID)
- `email` (for lookups)

---

## Collection: `invoices`

Stores invoice data extracted from uploaded images.

### Document Structure
```javascript
{
  id: string,                     // Unique invoice document ID
  userId: string,                 // Reference to user who uploaded
  invoiceNumber: string,          // Invoice number from document
  date: Timestamp,                // Invoice date
  vendorName: string,             // Vendor/supplier name
  vendorGSTIN: string,            // Vendor GSTIN
  totalAmount: number,            // Total invoice amount
  taxableAmount: number,          // Taxable amount
  gstAmount: number,              // Total GST amount
  items: Array<InvoiceItem>,      // Invoice line items
  imageUrl: string,               // Storage URL of invoice image
  extractionConfidence: number,   // AI extraction confidence (0-100)
  status: string,                 // 'pending' | 'processed' | 'verified'
  createdAt: Timestamp,           // Upload timestamp
  updatedAt: Timestamp            // Last update timestamp
}

// InvoiceItem structure
{
  description: string,
  quantity: number,
  rate: number,
  amount: number,
  gstRate: number,
  gstAmount: number
}
```

### Example Document
```json
{
  "id": "inv_abc123",
  "userId": "abc123xyz",
  "invoiceNumber": "INV-2024-001",
  "date": "2024-01-10T00:00:00Z",
  "vendorName": "XYZ Suppliers",
  "vendorGSTIN": "27YYYYY5678Y1Z9",
  "totalAmount": 11800,
  "taxableAmount": 10000,
  "gstAmount": 1800,
  "items": [
    {
      "description": "Product A",
      "quantity": 10,
      "rate": 1000,
      "amount": 10000,
      "gstRate": 18,
      "gstAmount": 1800
    }
  ],
  "imageUrl": "gs://bucket/invoices/abc123xyz/img_001.jpg",
  "extractionConfidence": 87,
  "status": "processed",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:35:00Z"
}
```

### Indexes
- `userId` + `createdAt` (descending) - for user's invoice list
- `userId` + `status` - for filtering by status

---

## Collection: `gstr1_drafts`

Stores generated GSTR-1 draft returns.

### Document Structure
```javascript
{
  id: string,                     // Unique draft ID
  userId: string,                 // Reference to user
  period: string,                 // Tax period (MM-YYYY)
  gstin: string,                  // Business GSTIN
  entries: Array<GSTR1Entry>,     // Array of GSTR-1 entries
  totalTaxableValue: number,      // Total taxable value
  totalIGST: number,              // Total IGST amount
  totalCGST: number,              // Total CGST amount
  totalSGST: number,              // Total SGST amount
  status: string,                 // 'draft' | 'reviewed' | 'exported'
  createdAt: Timestamp,           // Creation timestamp
  updatedAt: Timestamp            // Last update timestamp
}

// GSTR1Entry structure
{
  invoiceId: string,
  gstin: string,
  invoiceNumber: string,
  invoiceDate: Timestamp,
  taxableValue: number,
  igst: number,
  cgst: number,
  sgst: number
}
```

### Example Document
```json
{
  "id": "draft_xyz789",
  "userId": "abc123xyz",
  "period": "01-2024",
  "gstin": "27XXXXX1234X1Z5",
  "entries": [
    {
      "invoiceId": "inv_abc123",
      "gstin": "27YYYYY5678Y1Z9",
      "invoiceNumber": "INV-2024-001",
      "invoiceDate": "2024-01-10T00:00:00Z",
      "taxableValue": 10000,
      "igst": 1800,
      "cgst": 0,
      "sgst": 0
    }
  ],
  "totalTaxableValue": 10000,
  "totalIGST": 1800,
  "totalCGST": 0,
  "totalSGST": 0,
  "status": "draft",
  "createdAt": "2024-01-15T11:00:00Z",
  "updatedAt": "2024-01-15T11:00:00Z"
}
```

### Indexes
- `userId` + `period` - for finding drafts by period
- `userId` + `createdAt` (descending) - for listing recent drafts

---

## Collection: `copilot_chats`

Stores AI copilot chat sessions and messages.

### Document Structure
```javascript
{
  id: string,                     // Unique chat session ID
  userId: string,                 // Reference to user
  contextType: string,            // 'invoice' | 'gstr1' | 'general'
  contextId: string,              // Reference to invoice or draft ID (optional)
  messages: Array<Message>,       // Array of chat messages
  createdAt: Timestamp,           // Session creation timestamp
  updatedAt: Timestamp            // Last message timestamp
}

// Message structure
{
  role: string,                   // 'user' | 'assistant'
  content: string,                // Message content
  timestamp: Timestamp            // Message timestamp
}
```

### Example Document
```json
{
  "id": "chat_qwe456",
  "userId": "abc123xyz",
  "contextType": "gstr1",
  "contextId": "draft_xyz789",
  "messages": [
    {
      "role": "user",
      "content": "What is the total GST for this month?",
      "timestamp": "2024-01-15T11:30:00Z"
    },
    {
      "role": "assistant",
      "content": "The total GST for January 2024 is ₹1,800 (IGST).",
      "timestamp": "2024-01-15T11:30:02Z"
    }
  ],
  "createdAt": "2024-01-15T11:30:00Z",
  "updatedAt": "2024-01-15T11:30:02Z"
}
```

### Indexes
- `userId` + `updatedAt` (descending) - for listing recent chats
- `userId` + `contextType` + `contextId` - for finding context-specific chats

---

## Security Rules

All collections follow these security principles:

1. **Authentication Required**: All operations require a valid Firebase Auth token
2. **User Isolation**: Users can only access their own data (`userId` field)
3. **Read Access**: Users can read their own documents
4. **Write Access**: Users can create, update, and delete their own documents

See `firebase/firestore.rules` for complete security rules.

---

## Storage Structure

Firebase Storage is organized as follows:

```
gs://bucket-name/
├── invoices/
│   └── {userId}/
│       └── {fileName}           # Invoice images
└── profiles/
    └── {userId}/
        └── {fileName}           # Profile pictures
```

### Storage Rules
- Users can only access their own files
- Maximum file size: 10MB for invoices, 5MB for profiles
- Only image files allowed
