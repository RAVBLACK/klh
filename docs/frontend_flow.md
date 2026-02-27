# Frontend Flow

## User Journey

### 1. Landing & Authentication

#### Home Page (`/`)
- **Not Logged In**: 
  - Show About section
  - Features overview
  - "Get Started" button → Login page
  
- **Logged In**:
  - Redirect to Shop Dashboard

#### Login/Signup (`/login`, `/signup`)
- Firebase Authentication
- Email/Password or Phone OTP
- On success → Check if first-time user

### 2. First-Time Setup (`/setup`)

**Triggered**: New users with no shops

**Steps**:
1. **Shop Name**: Enter business name
2. **Shop Type**: Select type (Retail, Wholesale, Service, Manufacturing)
3. **Customer Name**: Enter customer/owner name
4. **First Month**: Select starting month

**On Complete**: → Shop Dashboard

### 3. Shop Dashboard (`/shops`)

**Display**:
- Grid of all user's shops
- Each shop card shows:
  - Shop name
  - Shop type
  - Customer name
  - Created date
- "Add Shop" button

**Actions**:
- Click shop card → Month Dashboard
- Add new shop → Add Shop Modal

### 4. Month Dashboard (`/shop/:shopId/months`)

**Display**:
- Shop name in navbar
- Back button to Shop Dashboard
- Grid of months for selected shop
- Each month card shows:
  - Month name
  - Invoice count
  - Created date
- "Add Month" button

**Actions**:
- Click month card → Upload Invoice page
- Add new month → Add Month Modal

### 5. Upload Invoice (`/shop/:shopId/month/:monthId/upload`)

**Features**:
- **Camera Capture**: Native mobile camera
- **Gallery Upload**: Select from phone
- **Preview**: Show captured image
- **Submit**: Upload and process

**Flow**:
1. Capture/Select image
2. Preview & confirm
3. Upload to backend
4. Processing (show loader)
5. → Invoice Result page

### 6. Invoice Result (`/invoice/:invoiceId`)

**Display**:
- Extracted invoice data
- Confidence scores (color-coded badges)
- **Editable fields**: Click to edit
- Invoice classification (B2B/B2C)
- Line items table

**Actions**:
- Edit fields
- Save changes
- Ask Copilot questions
- View GSTR-1 Preview

### 7. GSTR-1 Preview (`/month/:monthId/gstr1`)

**Display**:
- Monthly summary
- B2B invoices table
- B2C Large invoices table
- B2C Small summary
- Totals:
  - Total Taxable Value
  - Total CGST
  - Total SGST
  - Total IGST
  - Total Tax

**Actions**:
- Download CSV
- Edit invoices
- Generate final report

### 8. Profile (`/profile`)

**Display**:
- User information
- Settings
- Language preference
- Logout button

## Navigation Structure

```
Home (/)
├── Login (/login)
└── Signup (/signup)

Shop Dashboard (/shops) ← Default after login
├── Add Shop Modal
└── Shop Card Click
    └── Month Dashboard (/shop/:shopId/months)
        ├── Add Month Modal
        └── Month Card Click
            └── Upload Invoice (/shop/:shopId/month/:monthId/upload)
                └── Invoice Result (/invoice/:invoiceId)
                    ├── AI Copilot Chat
                    └── GSTR-1 Preview (/month/:monthId/gstr1)
                        └── Download CSV

Profile (/profile)
```

## Bottom Navigation

**Icons** (visible on all main pages):
1. 🏠 **Home**: → Shop Dashboard
2. 📤 **Upload**: → Upload Invoice (needs shop/month context)
3. 📊 **Reports**: → GSTR-1 Preview (needs month context)
4. 👤 **Profile**: → Profile page

## State Management

### Auth Context
- Current user
- Login/Logout functions
- Token management

### Shop Context
- List of shops
- Current selected shop
- Months for current shop
- CRUD operations

### Invoice Context
- Invoices for current month
- Upload status
- Extracted data

## Mobile-First Considerations

1. **Touch Targets**: Minimum 44px
2. **Bottom Navigation**: Easy thumb access
3. **Camera Integration**: Native camera API
4. **Offline Support**: PWA caching
5. **Responsive**: 320px to 428px width
6. **Pull to Refresh**: On list pages
7. **Swipe Gestures**: Back navigation

## Error Handling

1. **Network Errors**: Retry mechanism
2. **Upload Failures**: Show error, allow retry
3. **Invalid Data**: Highlight fields
4. **Session Timeout**: Redirect to login

## Loading States

1. **Page Load**: Full-screen loader
2. **Data Fetch**: Skeleton screens
3. **Image Upload**: Progress bar
4. **Processing**: "Analyzing invoice..." with spinner
