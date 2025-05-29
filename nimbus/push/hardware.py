from pydantic import BaseModel, ConfigDict

from nimbus.util import to_cgminer


class NimbusPushHardware(BaseModel):
    """
    Hardware information for the push model.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    make: str
    """
    The make of the miner.
    This should be something like `"Antminer"`, `"Whatsminer"`, or `"Avalonminer"`.
    """
    model: str
    """
    The model of the miner.
    This should be something like `"S9"`, `"M30S++VH30"`, or `"A1246"`.
    """
    chips: int
    """
    The total expected number of chips across all boards.
    """
    cores: int
    """
    The total expected number of core across all chips on all boards.
    """
    boards: int
    """
    The total expected number of boards.
    """
    fans: int
    """
    The total expected number of fans.
    """
    board_chips: list[int]
    """
    The chips expected on each board, in order by board ID.
    This will be the same chip count for all boards for most devices, but some may have different chip counts per board.
    This should be somthing like `[63, 63, 63]`.
    """
    algo: str
    """
    The algorithm this device is mining.
    This should be something like `"SHA256"`.
    """
