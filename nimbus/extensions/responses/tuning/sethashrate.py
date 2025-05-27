from pydantic import BaseModel, ConfigDict

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import to_cgminer


class NimbusSetHashrateResult(BaseModel):
    """
    The result of the set hashrate command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    target: int
    """
    The hashrate target being set.
    """


class NimbusSetHashrateCommandResult(NimbusBaseCommandResult):
    """
    Set hashrate command result.
    """

    sethashrate: list[NimbusSetHashrateResult]
    """
    The result of the sethashrate command.
    """
