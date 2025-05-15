from datetime import UTC, datetime


def parse_unix_timestamp(value: int | datetime) -> datetime:
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=UTC)
    return value
