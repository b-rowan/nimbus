from enum import StrEnum
from typing import Any

from pydantic import BaseModel


class NimbusPushEvent(StrEnum):
    STARTING = "starting"
    DATA = "data"
    STOPPING = "stopping"


class NimbusPushMessage(BaseModel):
    event: NimbusPushEvent
    value: Any
