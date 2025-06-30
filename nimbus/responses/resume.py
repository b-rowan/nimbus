from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, field_serializer

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util import parse_unix_timestamp, to_cgminer


class NimbusResumeResult(BaseModel):
    """
    The result of the resume command.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    when: Annotated[datetime, BeforeValidator(parse_unix_timestamp)]
    """
    When the resume will occur as UNIX timestamp in seconds.
    """

    @field_serializer("when")
    def serialize_when(self, when: datetime, _info) -> int:
        return int(when.timestamp())


class NimbusResumeCommandResult(NimbusBaseCommandResult):
    """
    Resume command result.
    """

    resume: list[NimbusResumeResult]
    """
    The result of the resume command.
    """
