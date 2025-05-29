from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from nimbus.push.hashrate import NimbusHashrate
from nimbus.util import to_cgminer


class NimbusPushHashboards(BaseModel):
    """
    Hashboard data for the push model.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    id: int = Field(
        serialization_alias="ID",
        validation_alias=AliasChoices("id", "ID"),
    )
    """
    The board ID, indexed from 0.
    For example, for an S9 with connectors labeled 6/7/8, 6 is 0, 7 is 1, and 8 is 2.
    """
    chips: int
    """
    The number of chips on this board.
    """
    cores: int
    """
    The total number of cores across all chips.
    """
    driver: str
    """
    The driver being used for this board.
    This value should be the same as the name of the mining process, for CGMiner this would be set to `"cgminer"`
    """
    working_chips: int
    """
    The number of working chips on this board.
    """
    expected_hashrate: float
    """
    The expected hashrate of the board.
    """
    serial_number: str | None = None
    """
    The serial number of the board if applicable.
    """
    voltage: float
    """
    The voltage of the board, in volts.
    """
    frequency: float
    """
    The clock speed of the board, in MHz.
    """
    wattage: int
    """
    The total power draw of the board in watts.
    """
    wattage_limit: int
    """
    The maximum power draw of the board.
    """
    hashrate_1m: NimbusHashrate
    """
    The average hashrate of the board since 1 minute ago.
    This should be used as the "real hashrate" of the board by the end user.
    """
    hashrate_5m: NimbusHashrate
    """
    The average hashrate of the board since 5 minutes ago.
    """
    hashrate_15m: NimbusHashrate
    """
    The average hashrate of the board since 15 minutes ago.
    """
    active: bool
    """
    Whether the board is active.
    """
    pcb_temperature: float = Field(
        serialization_alias="PCB Temperature",
        validation_alias=AliasChoices("pcb_temperature", "PCB Temperature"),
    )
    """
    The PCB temperature of the board.
    """
    intake_temperature: float
    """
    The intake temperature of the board.
    This is usually sourced from the first sensor on the board.
    """
    outlet_temperature: float
    """
    The outlet temperature of the board.
    This is usually sourced from the last sensor on the board.
    """
    tuned: bool
    """
    Whether this board is fully tuned.
    The meaning of this field is very implementation specific, but should be used to indicate that the board is currently at "nominal".
    """
