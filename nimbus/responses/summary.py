from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import (
    AliasChoices,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    field_serializer,
)
from pydantic.alias_generators import to_pascal

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util.time import parse_unix_timestamp


class NimbusMinerMessageSeverity(StrEnum):
    """
    CGMiner compatible status code.

    Attributes:
        INFO: Information message, used to inform the user of some state which is not having a noticeable effect.
        WARNING: Warning message, used to inform the user of some state which may cause a noticeable effect.
        ERROR: Error message, used to inform the user of some state which is causing a noticeable effect.
        FATAL: Fatal message, used to inform the user of some state which will prevent mining altogether.
    """

    FATAL = "Fatal"
    ERROR = "Error"
    WARNING = "Warning"
    INFO = "Info"


class NimbusMinerMessage(BaseModel):
    """
    Miner messages, representing different state information.

    Attributes:
        when: When the message was initiated, as a UNIX timestamp in seconds.
        code: A numerical code representing this specific error.
            This value may be set to `None` if there is no applicable code.
        message: The message describing the state information.
        severity: The severity of the message.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    code: int | None = None
    message: str
    severity: NimbusMinerMessageSeverity

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusSummaryResult(BaseModel):
    """
    Partially CGMiner compatible mining summary.

    This result is partially compatible due to the removal of the majority of the information from the CGMiner standard.
    Any missing data may be added at the prerogative of the implementor.

    Attributes:
        elapsed: The time elapsed since the miner started mining in seconds.
        uptime: The total uptime of the system in seconds.
        mhs_avg: The average hashrate of the miner in MH/s since the start of the `elapsed` timer.
        mhs_1m: The average hashrate of the miner in MH/s since 1 minute ago.
            This should be used as the "real hashrate" of the miner by the end user.
        mhs_5m: The average hashrate of the miner in MH/s since 5 minutes ago.
        mhs_15m: The average hashrate of the miner in MH/s since 15 minutes ago.
        mac: The MAC address or hardware address of the miner.
            This should be in the format `"11:22:33:44:55:66"`.
        serial_number: The serial number of the miner if applicable.
        control_board: The control board type of the miner, if applicable.
            This should be something like `"AMLogic"` or `"H616"`.
        fans: The current RPM of the fans, in order.
            This must be the same length as the number of fans defined in the `hardware` command.
            For fans which are not responding or have failed, use `None`.
        fan_speed: The fan speed being targeted at this moment.
            This value should be as a percentage, such as `100` or `50` percent speed.
            For devices which have had fans removed for immersion, set this to `0`.
        psu_fans: The current RPM of the PSU fans, in order.
            This may be left as an empty list if there are no PSU fan readings.
        psu_fan_speed: The PSU fan speed being targeted at this moment.
            This value should be as a percentage, such as `100` or `50` percent speed.
            For devices with no PSU fans, set this to `None`.
            For devices which have PSU fans but no communication with them, set this to `100`.
        chip_temperature_avg: The average temperature of all chips on the miner in degrees C.
        board_temperature_avg: The average temperature of all boards on the miner in degrees C.
        fluid_temperature: The temperature of the fluid the miner is in.
            For air cooled devices, this is the environmental temperature, or the first sensor value if available.
            For immersion devices, this is the immersion fluid temperature, or the first sensor value if available.
            For hydro devices, this is the water temperature, or the first sensor value if available.
        wattage: The total power draw of the miner in watts.
        wattage_limit: The maximum power draw of the miner.
            For devices with auto-tuning, this should be set to the auto-tuning power limit.
            For devices with power modes or presets, this should be set to the estimated max power of that preset.
            For all other devices, this should be set to the PSU maximum rated power, or similar reasonable value.
        is_mining: Whether the device is currently mining.
        messages: A list of messages to explain the state of the device.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    elapsed: int
    uptime: int
    mhs_avg: int = Field(
        serialization_alias="MHS av",
        validation_alias=AliasChoices("mhs_avg", "MHS av"),
    )
    mhs_1m: int = Field(
        serialization_alias="MHS 1m",
        validation_alias=AliasChoices("mhs_1m", "MHS 1m"),
    )
    mhs_5m: int = Field(
        serialization_alias="MHS 5m",
        validation_alias=AliasChoices("mhs_5m", "MHS 5m"),
    )
    mhs_15m: int = Field(
        serialization_alias="MHS 15m",
        validation_alias=AliasChoices("mhs_15m", "MHS 15m"),
    )
    mac: str = Field(
        serialization_alias="MAC",
        validation_alias=AliasChoices("mac", "MAC"),
    )
    serial_number: str | None = None
    control_board: str | None = None
    fans: list[int | None] = Field(default_factory=list)
    fan_speed: int = 0
    psu_fans: list[int | None] = Field(default_factory=list)
    psu_fan_speed: int | None = None
    chip_temperature_avg: float
    board_temperature_avg: float
    fluid_temperature: float | None
    wattage: int
    wattage_limit: int
    is_mining: bool
    messages: list[NimbusMinerMessage]


class NimbusSummaryCommandResult(NimbusBaseCommandResult):
    """
    Partially CGMiner compatible summary command result.

    Attributes:
        summary: The result of the summary command. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    summary: list[NimbusSummaryResult] = Field(
        serialization_alias="SUMMARY",
        validation_alias=AliasChoices("summary", "SUMMARY"),
    )
