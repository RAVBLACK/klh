# GST Filing Copilot

## Project Overview

A mobile-first AI-powered GST filing copilot that helps businesses streamline their GST return filing process. The application allows users to capture invoice images, extract data using AI, and generate GSTR-1 drafts with an interactive copilot assistant.

## Tech Stack

### Frontend
- **React** with Vite for fast development
- **PWA-ready** for mobile-first experience
- **Firebase Authentication** for user management
- **Firestore** for real-time data storage

### Backend
- **FastAPI** (Python) for high-performance API
- **Firebase Admin SDK** for secure backend operations
- **OCR & AI** integration for invoice data extraction

### Database & Auth
- **Firebase Authentication** for secure user login
- **Cloud Firestore** for NoSQL database
- **Firebase Storage** for invoice images

## Folder Structure

```
gst-filing-copilot/
├── frontend/          # React + Vite PWA
├── backend/           # FastAPI Python server
├── firebase/          # Firebase configuration & rules
├── docs/              # Documentation
├── scripts/           # Utility scripts
├── .env.example       # Environment variables template
└── README.md          # This file
```

## How to Run

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will run on `http://localhost:5173`

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend API will run on `http://localhost:8000`

## Firebase Setup

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Authentication (Email/Password)
3. Create a Firestore database
4. Enable Firebase Storage
5. Download the service account key for backend
6. Copy `.env.example` to `.env` and fill in your credentials

## Disclaimer

⚠️ **This application generates DRAFT GST returns only.**

The AI-extracted data should be reviewed and verified before filing with the GST portal. This tool is designed to assist, not replace, professional tax compliance processes.

## License

All rights reserved.
