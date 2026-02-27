"""
Helper Utilities
Common helper functions
"""

import hashlib
import uuid
from datetime import datetime
from typing import Any, Dict


def generate_id() -> str:
    """Generate unique ID"""
    return str(uuid.uuid4())


def hash_string(text: str) -> str:
    """Generate SHA256 hash of string"""
    return hashlib.sha256(text.encode()).hexdigest()


def current_timestamp() -> str:
    """Get current ISO timestamp"""
    return datetime.utcnow().isoformat()


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe storage"""
    # Remove special characters
    safe_chars = ('_', '-', '.')
    sanitized = ''.join(
        c if c.isalnum() or c in safe_chars else '_'
        for c in filename
    )
    return sanitized


def calculate_percentage(part: float, total: float) -> float:
    """Calculate percentage"""
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


def format_currency(amount: float) -> str:
    """Format amount as Indian currency"""
    return f"₹{amount:,.2f}"


def parse_indian_number(number_str: str) -> float:
    """Parse Indian number format (with commas)"""
    cleaned = number_str.replace(',', '').replace('₹', '').strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0
