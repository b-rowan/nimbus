from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
)

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


def validate_semantic_version(value: str):
    if not value.startswith("v"):
        raise ValueError("Value should be a semantic version.")
    return value


class NimbusDeviceDetailResult(BaseModel):
    """
    CGMiner compatible device details.

    Attributes:
        id: The board ID, indexed from 0.
            For example, for an S9 with connectors labeled 6/7/8, 6 is 0, 7 is 1, and 8 is 2.
        devdetails: The same value as ID, just included for CGMiner compatibility.
            Technically this could be different from ID in the original CGMiner code, but modern requirements make using 0 indexed values more useful.
        chips: The number of chips on this board.
        cores: The total number of cores across all chips.
        driver: The driver being used for this board.
            This value should be the same as the name of the mining process, for CGMiner this would be set to `"cgminer"`
        kernel: The name and version number of the kernel being used.
            This value is arbitrary, and will likely not be used by the end user.
        model: The model of the device this board is attached to.
            This value must match the `type` value of the [version command][nimbus.responses.version.NimbusVersionResult].
        working_chips: The number of working chips on this board.
        expected_hashrate: The expected hashrate of the board.
        serial_number: The serial number of the board.
        voltage: The voltage of the board, in volts.
        frequency: The clock speed of the board, in MHz.
        wattage: The total power draw of the board in watts.
        wattage_limit: The maximum power draw of the board.
        mhs_1m: The average hashrate of the board in MH/s since 1 minute ago.
            This should be used as the "real hashrate" of the board by the end user.
        mhs_5m: The average hashrate of the board in MH/s since 5 minutes ago.
        mhs_15m: The average hashrate of the board in MH/s since 15 minutes ago.
        active: Whether the board is active.
        pcb_temperature: The PCB temperature of the board.
        intake_temperature: The intake temperature of the board.
            This is usually sourced from the first sensor on the board.
        outlet_temperature: The outlet temperature of the board.
            This is usually sourced from the last sensor on the board.
        tuned: Whether this board is fully tuned.
            The meaning of this field is very implementation specific, but should be used to indicate that the board is currently at "nominal".
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    id: int = Field(
        serialization_alias="ID",
        validation_alias=AliasChoices("id", "ID"),
    )
    chips: int
    cores: int
    driver: str
    kernel: str | None = None
    model: str
    working_chips: int
    expected_hashrate: float
    serial_number: str | None = None
    voltage: float
    frequency: float
    wattage: int
    wattage_limit: int
    mhs_1m: float = Field(
        serialization_alias="MHS 1m",
        validation_alias=AliasChoices("mhs_1m", "MHS 1m"),
    )
    mhs_5m: float = Field(
        serialization_alias="MHS 5m",
        validation_alias=AliasChoices("mhs_5m", "MHS 5m"),
    )
    mhs_15m: float = Field(
        serialization_alias="MHS 15m",
        validation_alias=AliasChoices("mhs_15m", "MHS 15m"),
    )
    active: bool
    pcb_temperature: float = Field(
        serialization_alias="PCB Temperature",
        validation_alias=AliasChoices("pcb_temperature", "PCB Temperature"),
    )
    intake_temperature: float
    outlet_temperature: float
    tuned: bool

    @computed_field(alias="DEVDETAILS")
    @property
    def devdetails(self) -> int:
        return self.id


class NimbusDeviceDetailsCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible devdetails command result.

    Attributes:
        devdetails: The result of the devdetails command, one per board. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    devdetails: list[NimbusDeviceDetailResult]
