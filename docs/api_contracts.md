# API Contracts

## Base URL
```
Development: http://localhost:8000
Production: https://api.gst-copilot.com
```

## Authentication
All authenticated endpoints require a Firebase ID token in the Authorization header:
```
Authorization: Bearer <firebase_id_token>
```

---

## Auth Endpoints

### POST /auth/login
Login user with email and password.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "firebase_id_token",
  "user": {
    "uid": "user_id",
    "email": "user@example.com"
  }
}
```

### POST /auth/register
Register new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "businessName": "ABC Corp"
}
```

**Response:**
```json
{
  "uid": "user_id",
  "email": "user@example.com",
  "message": "User registered successfully"
}
```

---

## Invoice Endpoints

### POST /invoice/upload
Upload and process invoice image.

**Headers:**
```
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

**Request Body:**
```
file: <image_file>
```

**Response:**
```json
{
  "invoiceId": "inv_123",
  "status": "processing",
  "extractedData": {
    "invoiceNumber": "INV-001",
    "date": "2024-01-15",
    "vendorName": "Vendor Name",
    "vendorGSTIN": "27XXXXX1234X1Z5",
    "totalAmount": 11800,
    "items": [...]
  },
  "confidence": 85
}
```

### GET /invoice/{invoice_id}
Get invoice details by ID.

**Response:**
```json
{
  "id": "inv_123",
  "invoiceNumber": "INV-001",
  "date": "2024-01-15",
  "vendorName": "Vendor Name",
  "totalAmount": 11800,
  "status": "processed"
}
```

### GET /invoice/
List all invoices for authenticated user.

**Query Parameters:**
- `limit` (optional): Number of invoices to return (default: 20)
- `offset` (optional): Pagination offset (default: 0)
- `status` (optional): Filter by status

**Response:**
```json
{
  "invoices": [...],
  "total": 50,
  "limit": 20,
  "offset": 0
}
```

---

## GST Endpoints

### POST /gst/generate-gstr1
Generate GSTR-1 draft from selected invoices.

**Request Body:**
```json
{
  "invoiceIds": ["inv_1", "inv_2", "inv_3"],
  "period": "01-2024",
  "gstin": "27XXXXX1234X1Z5"
}
```

**Response:**
```json
{
  "draftId": "draft_123",
  "period": "01-2024",
  "entries": [...],
  "totals": {
    "taxableValue": 100000,
    "igst": 18000,
    "cgst": 0,
    "sgst": 0
  }
}
```

### GET /gst/gstr1/{draft_id}
Get GSTR-1 draft by ID.

**Response:**
```json
{
  "id": "draft_123",
  "period": "01-2024",
  "entries": [...],
  "status": "draft"
}
```

### POST /gst/export
Export GST data in specified format.

**Request Body:**
```json
{
  "draftId": "draft_123",
  "format": "json|excel|csv"
}
```

**Response:**
```json
{
  "downloadUrl": "https://storage.../export.xlsx",
  "expiresAt": "2024-01-20T10:00:00Z"
}
```

---

## Copilot Endpoints

### POST /copilot/chat
Send message to AI copilot.

**Request Body:**
```json
{
  "sessionId": "chat_123",
  "message": "What is the total GST for this month?",
  "context": {
    "type": "gstr1",
    "id": "draft_123"
  }
}
```

**Response:**
```json
{
  "sessionId": "chat_123",
  "response": "Based on the GSTR-1 draft, the total GST for January 2024 is ₹18,000.",
  "suggestions": [
    "View detailed breakdown",
    "Export to Excel"
  ]
}
```

### GET /copilot/history/{session_id}
Get chat history for a session.

**Response:**
```json
{
  "sessionId": "chat_123",
  "messages": [
    {
      "role": "user",
      "content": "What is the total GST?",
      "timestamp": "2024-01-15T10:00:00Z"
    },
    {
      "role": "assistant",
      "content": "The total GST is ₹18,000.",
      "timestamp": "2024-01-15T10:00:01Z"
    }
  ]
}
```

---

## Error Responses

All endpoints may return the following error format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {}
  }
}
```

### Common Error Codes
- `AUTH_REQUIRED` - Authentication required
- `INVALID_TOKEN` - Invalid or expired token
- `NOT_FOUND` - Resource not found
- `VALIDATION_ERROR` - Input validation failed
- `INTERNAL_ERROR` - Server error
