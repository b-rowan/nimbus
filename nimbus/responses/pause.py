from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, field_serializer

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import parse_unix_timestamp, to_cgminer


class NimbusPauseResult(BaseModel):
    """
    The result of the pause command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    """
    When the pause will occur as UNIX timestamp in seconds.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusPauseCommandResult(NimbusBaseCommandResult):
    """
    Pause command result.
    """

    pause: list[NimbusPauseResult]
    """
    The result of the pause command.
    """
