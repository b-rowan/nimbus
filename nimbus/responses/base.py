from datetime import datetime, UTC
from enum import StrEnum
from importlib.metadata import version
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    field_serializer,
    BeforeValidator,
    AliasChoices,
    ConfigDict,
    RootModel,
)
from pydantic.alias_generators import to_pascal


def parse_unix_timestamp(value: int | datetime) -> datetime:
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=UTC)
    return value


class NimbusStatusCode(StrEnum):
    """
    CGMiner compatible status code.
    """

    WARNING = "W"
    INFO = "I"
    SUCCESS = "S"
    ERROR = "E"
    FATAL = "F"


class NimbusCommandStatus(BaseModel):
    """
    CGMiner compatible status information.

    Attributes:
        status: One of `WARNING` - "W", `INFO` - "I", `SUCCESS` - "S", `ERROR` - "E", `FATAL` - "F"
        when: UNIX timestamp in seconds
        code: A status code for the command
            This value is not used as part of the schema defined by `nimbus`, but is left in for CGMiner compatibility, and so defaults to 1.
        msg: A message for the command
            This value is not strictly defined by `nimbus`, but should be a short user readable message explaining the result of the command.
        description: A description to accompany the command
            This value is nearly always used to hold the miner process version, such as `cgminer v1.0.0`.
        protocol: The protocol and version being used by this device
            Defaults to `nimbus v{version}`, but may be set to an alternate protocol if desired.
            For custom protocols which fully implement a version of `nimbus` and only add functionality, this should be suffixed, such as `nimbus v{version}.cgminer-1`

    Example:
        ```python
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
    """

    status: list[NimbusCommandStatus] = Field(
        serialization_alias="STATUS",
        validation_alias=AliasChoices("status", "STATUS"),
    )


class NimbusMultiCommandResult(RootModel):
    """
    CGMiner compatible multicommand result.

    This class should be used to represent the result of a multicommand.
    A multicommand is a `+` delimited list of commands, such as `devdetails+version`.
    """

    root: dict[str, NimbusBaseCommandResult]
