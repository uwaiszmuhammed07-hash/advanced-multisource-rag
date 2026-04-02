def clean_text(text: str) -> str:
    text = text.replace("\n", " ").replace("\t", " ")
    text = " ".join(text.split())
    return text