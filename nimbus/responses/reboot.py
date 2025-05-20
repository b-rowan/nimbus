from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, field_serializer

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import parse_unix_timestamp


class NimbusRebootResult(BaseModel):
    """
    The result of the reboot command.

    Attributes:
        when: When the reboot will occur as UNIX timestamp in seconds.
    """

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusRebootCommandResult(NimbusBaseCommandResult):
    """
    Reboot command result.

    Attributes:
        reboot: The result of the reboot command.
        status: A status result for the command being sent. CGMiner compatible.
    """

    reboot: list[NimbusRebootResult]
