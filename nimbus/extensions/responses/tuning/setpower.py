from pydantic import BaseModel, ConfigDict

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import to_cgminer


class NimbusSetPowerResult(BaseModel):
    """
    The result of the set power command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    target: int
    """
    The power target being set.
    """


class NimbusSetPowerCommandResult(NimbusBaseCommandResult):
    """
    Set power command result.
    """

    setpower: list[NimbusSetPowerResult]
    """
    The result of the setpower command.
    """
