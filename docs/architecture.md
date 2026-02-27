# System Architecture

## Overview

The GST Filing Copilot is a mobile-first, AI-powered application designed to streamline GST filing for businesses. The system uses a modern, scalable architecture with clear separation of concerns.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         React PWA (Vite)                            │   │
│  │  - Camera Capture                                    │   │
│  │  - Invoice Management                                │   │
│  │  - AI Copilot Interface                             │   │
│  │  - GSTR-1 Preview                                   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTPS/REST
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         FastAPI Backend (Python)                    │   │
│  │                                                      │   │
│  │  API Routes:                                        │   │
│  │  - Auth Routes                                       │   │
│  │  - Invoice Routes                                    │   │
│  │  - GST Routes                                        │   │
│  │  - Copilot Routes                                    │   │
│  │                                                      │   │
│  │  Services:                                          │   │
│  │  - Image Preprocessing                               │   │
│  │  - OCR Service                                       │   │
│  │  - AI Extraction                                     │   │
│  │  - GST Logic                                         │   │
│  │  - Copilot Service                                   │   │
│  │  - Export Service                                    │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATA LAYER                               │
│                                                              │
│  ┌──────────────────┐  ┌──────────────────┐               │
│  │ Firebase Auth    │  │  Cloud Firestore │               │
│  │                  │  │                  │               │
│  │ - User Auth      │  │ - Users          │               │
│  │ - Token Mgmt     │  │ - Invoices       │               │
│  └──────────────────┘  │ - GSTR1 Drafts   │               │
│                        │ - Copilot Chats  │               │
│  ┌──────────────────┐  └──────────────────┘               │
│  │Firebase Storage  │                                       │
│  │                  │                                       │
│  │ - Invoice Images │                                       │
│  │ - User Assets    │                                       │
│  └──────────────────┘                                       │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool and dev server
- **Firebase SDK** - Authentication and Firestore integration
- **PWA** - Progressive Web App capabilities

### Backend
- **FastAPI** - High-performance Python web framework
- **Firebase Admin SDK** - Server-side Firebase operations
- **OCR Libraries** - Text extraction from images
- **AI/ML Services** - Data extraction and copilot functionality

### Database & Storage
- **Firebase Authentication** - User management
- **Cloud Firestore** - NoSQL database
- **Firebase Storage** - File storage

## Data Flow

### 1. Invoice Processing Flow
```
User Captures Image → Upload to Storage → Preprocessing → 
OCR Extraction → AI Data Extraction → Validation → 
Store in Firestore → Display Results
```

### 2. GST Filing Flow
```
Select Invoices → Validate Data → Generate GSTR-1 → 
AI Review (Copilot) → User Review → Export
```

### 3. Copilot Interaction Flow
```
User Query → Context Analysis → AI Processing → 
Response Generation → Display to User
```

## Security Considerations

1. **Authentication**: Firebase Authentication with email/password
2. **Authorization**: Firestore security rules for data access control
3. **Data Privacy**: User data isolated by UID
4. **Secure Communication**: HTTPS for all API calls
5. **Input Validation**: Server-side validation for all inputs

## Scalability

- **Horizontal Scaling**: FastAPI can be deployed across multiple instances
- **Database**: Firestore scales automatically
- **Caching**: Implement Redis for frequently accessed data (future)
- **CDN**: Static assets served via Firebase Hosting

## Future Enhancements

- Multi-file upload
- Bulk processing
- Advanced analytics dashboard
- Integration with GST portal
- Multiple language support
