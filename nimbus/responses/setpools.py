from pydantic import BaseModel, ConfigDict

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import to_cgminer


class NimbusSetPoolsResult(BaseModel):
    """
    The result of the set pools command.

    Attributes:
        groups: The number of groups being set.
        pools: The number of pools being set.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    groups: int
    pools: int


class NimbusSetPoolsCommandResult(NimbusBaseCommandResult):
    """
    Set pools command result.

    Attributes:
        setpools: The result of the setpools command.
        status: A status result for the command being sent. CGMiner compatible.
    """

    setpools: list[NimbusSetPoolsResult]
