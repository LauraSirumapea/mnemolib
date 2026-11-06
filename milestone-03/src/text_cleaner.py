import re

def clean_text(text: str) -> str:
    """Normalize extracted text while retaining paragraph boundaries and Indonesian terms."""
    if not text:
        return ""
    text = text.replace("\x00", " ").replace("\ufeff", " ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
