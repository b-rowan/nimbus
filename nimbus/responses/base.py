from datetime import datetime, UTC
from enum import Enum
from importlib.metadata import version
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    field_serializer,
    BeforeValidator,
    AliasChoices,
    ConfigDict,
)
from pydantic.alias_generators import to_pascal


def parse_unix_timestamp(value: int | datetime) -> datetime:
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=UTC)
    return value


class NimbusStatusCode(Enum):
    """
    CGMiner compatible status code.

    Attributes:
        INFO: Information message, should be used for commands which do not modify the state of the device (read-only).  Treated as a success.
        WARNING: Warning message, should be used for commands which do not modify the state of the device (read-only).  Should also be used to indicate an invalid command.
        SUCCESS: Success message, should be used for commands which modify the state of the device (write).
        ERROR: Error message, should be used when something went wrong when modifying the state of the device (write).
        FATAL: Fatal message, should be used to indicate an internal error on the device which was unexpected.
    """

    INFO = "I"
    WARNING = "W"
    SUCCESS = "S"
    ERROR = "E"
    FATAL = "F"


class NimbusCommandStatus(BaseModel):
    """
    CGMiner compatible status information.

    Attributes:
        status: The status of the command.
        when: UNIX timestamp in seconds.
        code: A status code for the command.
            This value is not used as part of the schema defined by `nimbus`, but is left in for CGMiner compatibility, and so defaults to 1.
        msg: A message for the command.
            This value is not strictly defined by `nimbus`, but should be a short user readable message explaining the result of the command.
        description: A description to accompany the command.
            This value is nearly always used to hold the miner process version, such as `cgminer v1.0.0`.
        protocol: The protocol and version being used by this device.
            Defaults to `nimbus v{version}`, but may be set to an alternate protocol if desired.
            For custom protocols which fully implement a version of `nimbus` and only add functionality, this should be suffixed, such as `nimbus v{version}.cgminer-1`

    Example:
        ```python3
        command_status = NimbusCommandStatus(
            status = NimbusStatusCode.SUCCESS,
            msg = "Device details",
            description = "cgminer v1.0.0"
        )

        print(command_status.model_dump(by_alias=True))

        # {
        #     "STATUS": "S",
        #     "When": 1747157878,
        #     "Code": 1,
        #     "Msg": "Device details",
        #     "Description": "cgminer v1.0.0",
        #     "Protocol": "nimbus v1.0.0",
        # }
        ```
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    # a bit janky, but needs to be done this way for full type hinting
    status: NimbusStatusCode = Field(
        serialization_alias="STATUS",
        validation_alias=AliasChoices("status", "STATUS"),
    )
    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)] = Field(
        default_factory=lambda: datetime.now(UTC)
    )
    code: int = 1
    msg: str
    description: str
    protocol: str = f"nimbus v{version('nimbus')}"

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusBaseCommandResult(BaseModel):
    """
    CGMiner compatible base response.

    Attributes:
        status: A status result for the command being sent.  CGMiner compatible.
    """

    status: list[NimbusCommandStatus] = Field(
        serialization_alias="STATUS",
        validation_alias=AliasChoices("status", "STATUS"),
    )
