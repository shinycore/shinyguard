import datetime
from typing import Any


def process_date(date: Any) -> Any:
    if isinstance(date, str):
        return datetime.datetime.fromisoformat(date)
    elif isinstance(date, datetime.date):
        return datetime.datetime.combine(date, datetime.time())
    else:  # pragma: no cover
        return date
