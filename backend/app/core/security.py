"""
Security Module
Firebase authentication and security
"""

from fastapi import HTTPException, status
from typing import Dict
import firebase_admin
from firebase_admin import auth, credentials
from app.utils.config import settings


# Initialize Firebase Admin
if settings.FIREBASE_CREDENTIALS_PATH:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)


async def verify_firebase_token(token: str) -> Dict:
    """
    Verify Firebase ID token and return user info
    """
    try:
        decoded_token = auth.verify_id_token(token)
        
        return {
            'uid': decoded_token['uid'],
            'email': decoded_token.get('email'),
            'name': decoded_token.get('name'),
            'phone': decoded_token.get('phone_number')
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication token: {str(e)}"
        )


def create_custom_token(uid: str) -> str:
    """
    Create custom Firebase token for testing
    """
    try:
        custom_token = auth.create_custom_token(uid)
        return custom_token.decode('utf-8')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create custom token: {str(e)}"
        )
