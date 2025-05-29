def validate_semantic_version(value: str):
    if not value.startswith("v"):
        raise ValueError("Value should be a semantic version.")
    return value
