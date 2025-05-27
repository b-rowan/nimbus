from datetime import UTC, datetime
from enum import Enum
from importlib.metadata import version
from typing import Annotated

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    field_serializer,
)

from nimbus.util.serialize import to_cgminer, to_upper
from nimbus.util.time import parse_unix_timestamp


class NimbusStatusCode(Enum):
    """
    CGMiner compatible status code.
    """

    INFO = "I"
    """
    Information message, should be used for commands which do not modify the state of the device (read-only).  Treated as a success.
    """
    WARNING = "W"
    """
    Warning message, should be used for commands which do not modify the state of the device (read-only).  Should also be used to indicate an invalid command.
    """
    SUCCESS = "S"
    """
    Success message, should be used for commands which modify the state of the device (write).
    """
    ERROR = "E"
    """
    Error message, should be used when something went wrong when modifying the state of the device (write).
    """
    FATAL = "F"
    """
    Fatal message, should be used to indicate an internal error on the device which was unexpected.
    """


class NimbusCommandStatus(BaseModel):
    """
    CGMiner compatible status information.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    status: NimbusStatusCode = Field(alias="STATUS")
    """
    The status of the command.
    """
    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)] = Field(default_factory=lambda: datetime.now(UTC))
    """
    UNIX timestamp in seconds.
    """
    code: int = 1
    """
    A status code for the command.
    This value is not used as part of the schema defined by `nimbus`, but is left in for CGMiner compatibility, and so defaults to 1.
    """
    msg: str
    """
    A message for the command.
    This value is not strictly defined by `nimbus`, but should be a short user readable message explaining the result of the command.
    """
    description: str
    """
    A description to accompany the command.
    This value is nearly always used to hold the miner process version, such as `cgminer v1.0.0`.
    """
    protocol: str = f"nimbus v{version('nimbus')}"
    """
    The protocol and version being used by this device.
    Defaults to `nimbus v{version}`, but may be set to an alternate protocol if desired.
    For custom protocols which fully implement a version of `nimbus` and only add functionality, this should be suffixed, such as `nimbus v{version}.cgminer-1`
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusBaseCommandResult(BaseModel):
    """
    CGMiner compatible base response.
    """

    model_config = ConfigDict(alias_generator=to_upper, populate_by_name=True)

    status: list[NimbusCommandStatus]
    """
    A status result for the command being sent.  CGMiner compatible.
    """
