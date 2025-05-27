from pydantic import BaseModel, ConfigDict

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import to_cgminer


class NimbusSetPoolsResult(BaseModel):
    """
    The result of the set pools command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    groups: int
    """
    The number of groups being set.
    """
    pools: int
    """
    The number of pools being set.
    """


class NimbusSetPoolsCommandResult(NimbusBaseCommandResult):
    """
    Set pools command result.
    """

    setpools: list[NimbusSetPoolsResult]
    """
    The result of the setpools command.
    """
