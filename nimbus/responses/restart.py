from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, field_serializer

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import parse_unix_timestamp, to_cgminer


class NimbusRestartResult(BaseModel):
    """
    The result of the restart command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    """
    When the restart will occur as UNIX timestamp in seconds.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusRestartCommandResult(NimbusBaseCommandResult):
    """
    Restart command result.
    """

    restart: list[NimbusRestartResult]
    """
    The result of the restart command.
    """
