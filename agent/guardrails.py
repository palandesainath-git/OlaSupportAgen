import re

def mask_pii(text: str) -> str:
    """Mask 10-digit phone numbers."""
    return re.sub(r"\b\d{10}\b", "XXXXXXXXXX", text)

def detect_injection(text: str) -> bool:
    """Detect prompt injection attempts."""
    return any(k in text.lower() for k in ["ignore", "override", "system prompt"])

def apply_guardrails(query: str):
    masked = mask_pii(query)
    if detect_injection(masked):
        return {"error": "Prompt injection detected"}
    return {"query": masked}

