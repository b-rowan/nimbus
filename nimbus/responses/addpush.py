from pydantic import BaseModel, ConfigDict

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


class NimbusAddPushResult(BaseModel):
    """
    The result of the add push command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    name: str
    """
    The name of the push endpoint added.
    """


class NimbusAddPushCommandResult(NimbusBaseCommandResult):
    """
    Add push command result.
    """

    addpush: list[NimbusAddPushResult]
    """
    The result of the addpush command.
    """
