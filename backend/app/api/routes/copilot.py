"""
Copilot Routes
Handle AI copilot chat endpoints
"""

from fastapi import APIRouter

router = APIRouter(prefix="/copilot", tags=["copilot"])

@router.post("/chat")
def chat():
    """Send message to copilot"""
    pass

@router.get("/history/{session_id}")
def get_chat_history(session_id: str):
    """Get chat history"""
    pass
