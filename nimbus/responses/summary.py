from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult
from .common import NimbusMinerMessage


class NimbusSummaryResult(BaseModel):
    """
    Partially CGMiner compatible mining summary.

    This result is partially compatible due to the removal of the majority of the information from the CGMiner standard.
    Any missing data may be added at the prerogative of the implementor.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    elapsed: int
    """
    The time elapsed since the miner started mining in seconds.
    """
    uptime: int
    """
    The total uptime of the system in seconds.
    """
    mhs_avg: float = Field(alias="MHS av", title="MHS av")
    """
    The average hashrate of the miner in MH/s since the start of the `elapsed` timer.
    """
    mhs_1m: float = Field(alias="MHS 1m", title="MHS 1m")
    """
    The average hashrate of the miner in MH/s since 1 minute ago.
    This should be used as the "real hashrate" of the miner by the end user.
    """
    mhs_5m: float = Field(alias="MHS 5m", title="MHS 5m")
    """
    The average hashrate of the miner in MH/s since 5 minutes ago.
    """
    mhs_15m: float = Field(alias="MHS 15m", title="MHS 15m")
    """
    The average hashrate of the miner in MH/s since 15 minutes ago.
    """
    mac: str = Field(alias="MAC", title="MAC")
    """
    The MAC address or hardware address of the miner.
    This should be in the format `"11:22:33:44:55:66"`.
    """
    serial_number: str | None = None
    """
    The serial number of the miner if applicable.
    """
    control_board: str | None = None
    """
    The control board type of the miner, if applicable.
    This should be something like `"AMLogic"` or `"H616"`.
    """
    fans: list[int | None] = Field(default_factory=list)
    """
    The current RPM of the fans, in order.
    This must be the same length as the number of fans defined in the `hardware` command.
    For fans which are not responding or have failed, use `None`.
    """
    fan_speed: float = 0
    """
    The fan speed being targeted at this moment.
    This value should be as a percentage, such as `100` or `50` percent speed.
    For devices which have had fans removed for immersion, set this to `0`.
    """
    psu_fans: list[int | None] = Field(default_factory=list)
    """
    The current RPM of the PSU fans, in order.
    This may be left as an empty list if there are no PSU fan readings.
    """
    psu_fan_speed: float | None = None
    """
    The PSU fan speed being targeted at this moment.
    This value should be as a percentage, such as `100` or `50` percent speed.
    For devices with no PSU fans, set this to `None`.
    For devices which have PSU fans but no communication with them, set this to `100`.
    """
    chip_temperature_avg: float
    """
    The average temperature of all chips on the miner in degrees C.
    """
    board_temperature_avg: float
    """
    The average temperature of all boards on the miner in degrees C.
    """
    fluid_temperature: float | None
    """
    The temperature of the fluid the miner is in.
    For air cooled devices, this is the environmental temperature, or the first sensor value if available.
    For immersion devices, this is the immersion fluid temperature, or the first sensor value if available.
    For hydro devices, this is the water temperature, or the first sensor value if available.
    """
    wattage: int
    """
    The total power draw of the miner in watts.
    """
    wattage_limit: int
    """
    The maximum power draw of the miner.
    For devices with auto-tuning, this should be set to the auto-tuning power limit.
    For devices with power modes or presets, this should be set to the estimated max power of that preset.
    For all other devices, this should be set to the PSU maximum rated power, or similar reasonable value.
    """
    is_mining: bool
    """
    Whether the device is currently mining.
    """
    messages: list[NimbusMinerMessage]
    """
    A list of messages to explain the state of the device.
    """


class NimbusSummaryCommandResult(NimbusBaseCommandResult):
    """
    Partially CGMiner compatible summary command result.
    """

    summary: list[NimbusSummaryResult]
    """
    The result of the summary command. CGMiner compatible.
    """
