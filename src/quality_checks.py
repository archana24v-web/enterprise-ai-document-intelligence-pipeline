def validate_document(text: str, minimum_characters: int = 50) -> dict:
    clean_text = text.strip()
    return {
        "is_valid": len(clean_text) >= minimum_characters,
        "character_count": len(clean_text),
        "reason": "ok" if len(clean_text) >= minimum_characters else "document text is too short",
    }
