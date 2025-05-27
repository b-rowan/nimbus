from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, field_serializer

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import parse_unix_timestamp, to_cgminer


class NimbusRebootResult(BaseModel):
    """
    The result of the reboot command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    """
    When the reboot will occur as UNIX timestamp in seconds.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusRebootCommandResult(NimbusBaseCommandResult):
    """
    Reboot command result.
    """

    reboot: list[NimbusRebootResult]
    """
    The result of the reboot command.
    """
