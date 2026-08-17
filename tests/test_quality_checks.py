from src.quality_checks import validate_document


def test_valid_document():
    result = validate_document("x" * 60)
    assert result["is_valid"] is True


def test_short_document_fails():
    result = validate_document("too short")
    assert result["is_valid"] is False
