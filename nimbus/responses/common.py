from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, field_serializer

from nimbus.util.serialize import to_cgminer
from nimbus.util.time import parse_unix_timestamp


class NimbusMinerMessageSeverity(StrEnum):
    """
    CGMiner compatible status code.
    """

    FATAL = "Fatal"
    """
    Fatal message, used to inform the user of some state which will prevent mining altogether.
    """
    ERROR = "Error"
    """
    Error message, used to inform the user of some state which is causing a noticeable effect.
    """
    WARNING = "Warning"
    """
    Warning message, used to inform the user of some state which may cause a noticeable effect.
    """
    INFO = "Info"
    """
    Information message, used to inform the user of some state which is not having a noticeable effect.
    """


class NimbusMinerMessage(BaseModel):
    """
    Miner messages, representing different state information.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    """
    When the message was initiated, as a UNIX timestamp in seconds.
    """
    code: int | None = None
    """
    A numerical code representing this specific error.
    This value may be set to `None` if there is no applicable code.
    """
    message: str
    """
    The message describing the state information.
    """
    severity: NimbusMinerMessageSeverity
    """
    The severity of the message.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())
