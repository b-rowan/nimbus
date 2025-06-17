from pydantic import BaseModel, ConfigDict

from nimbus.responses.base import NimbusBaseCommandResult
from nimbus.util import to_cgminer


class NimbusDeletePushResult(BaseModel):
    """
    The result of the delete push command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    name: str
    """
    The name of the push endpoint deleted.
    """


class NimbusDeletePushCommandResult(NimbusBaseCommandResult):
    """
    Delete push command result.
    """

    delpush: list[NimbusDeletePushResult]
    """
    The result of the delpush command.
    """
