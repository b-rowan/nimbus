from datetime import UTC, datetime
from importlib.metadata import version
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, field_serializer

from nimbus.push.base import NimbusPushEvent, NimbusPushMessage
from nimbus.responses.common import NimbusMinerMessage
from nimbus.util.serialize import to_cgminer
from nimbus.util.time import parse_unix_timestamp
from nimbus.util.validate import validate_semantic_version

from .hardware import NimbusPushHardware
from .hashboards import NimbusPushHashboards


class NimbusPushData(BaseModel):
    """
    Push model for nimbus.

    This model is the data format for pushing data to a webhook.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    protocol: str = f"nimbus v{version('nimbus')}"
    """
    The protocol and version being used by this device.
    Defaults to `nimbus v{version}`, but may be set to an alternate protocol if desired.
    For custom protocols which fully implement a version of `nimbus` and only add functionality, this should be suffixed, such as `nimbus v{version}.cgminer-1`
    """
    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)] = Field(default_factory=lambda: datetime.now(UTC))
    """
    UNIX timestamp in seconds.
    """
    ip: str = Field(alias="IP", title="IP")
    """
    The current IP address of the device.
    """
    mac: str = Field(alias="MAC", title="MAC")
    """
    The MAC address of the device.
    """
    hardware: NimbusPushHardware
    """
    Hardware information for the device.
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
    api_version: Annotated[str, BeforeValidator(validate_semantic_version)] = Field(
        alias="API", default=f"v{version('nimbus')}", title="API"
    )
    """
    The version of the API, defaults to the nimbus version.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    miner_version: Annotated[str, BeforeValidator(validate_semantic_version)]
    """
    The version of the mining process, such as CGMiner.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    firmware_version: Annotated[str, BeforeValidator(validate_semantic_version)]
    """
    The version of the firmware.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    extensions: list[str] = Field(default_factory=list)
    """
    All supported extensions, such as `"tuning.power"`.
    """
    hashboards: list[NimbusPushHashboards]
    """
    Hashboard data for the device.
    """
    wattage: int
    """
    The total power draw of the device in watts.
    """
    wattage_limit: int
    """
    The maximum power draw of the device.
    For devices with auto-tuning, this should be set to the auto-tuning power limit.
    For devices with power modes or presets, this should be set to the estimated max power of that preset.
    For all other devices, this should be set to the PSU maximum rated power, or similar reasonable value.
    """
    fluid_temperature: float | None
    """
    The temperature of the fluid the device is in.
    For air cooled devices, this is the environmental temperature, or the first sensor value if available.
    For immersion devices, this is the immersion fluid temperature, or the first sensor value if available.
    For hydro devices, this is the water temperature, or the first sensor value if available.
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
    is_mining: bool
    """
    Whether the device is currently mining.
    """
    messages: list[NimbusMinerMessage]
    """
    A list of messages to explain the state of the device.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusPushDataMessage(NimbusPushMessage):
    event: NimbusPushEvent = Field(default=NimbusPushEvent.DATA, init=False)
    value: NimbusPushData
