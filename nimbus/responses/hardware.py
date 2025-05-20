from pydantic import BaseModel, ConfigDict

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


class NimbusHardwareResult(BaseModel):
    """
    Hardware information.

    Attributes:
        make: The make of the miner.
            This should be something like `"Antminer"`, `"Whatsminer"`, or `"Avalonminer"`.
        model: The model of the miner.
            This should be something like `"S9"`, `"M30S++VH30"`, or `"A1246"`.
        chips: The total expected number of chips across all boards.
        cores: The total expected number of core across all chips on all boards.
        boards: The total expected number of boards.
        fans: The total expected number of fans.
        board_chips: The chips expected on each board, in order by board ID.
            This will be the same chip count for all boards for most devices, but some may have different chip counts per board.
            This should be somthing like `[63, 63, 63]`.
        algo: The algorithm this device is mining.
            This should be something like `"SHA256"`.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    make: str
    model: str
    chips: int
    cores: int
    boards: int
    fans: int
    board_chips: list[int]
    algo: str


class NimbusHardwareCommandResult(NimbusBaseCommandResult):
    """
    Hardware command result.

    Attributes:
        hardware: The result of the hardware command.
        status: A status result for the command being sent. CGMiner compatible.
    """

    hardware: list[NimbusHardwareResult]
