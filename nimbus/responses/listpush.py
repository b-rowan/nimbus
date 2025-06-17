from pydantic import AnyHttpUrl, BaseModel, ConfigDict

from nimbus.push.base import NimbusPushEvent
from nimbus.responses import NimbusBaseCommandResult


class NimbusPushLocation(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    """
    The name of the push location.
    """
    endpoint: AnyHttpUrl
    """
    The web endpoint to push data to.
    Data is sent via a POST request.
    """
    frequency: int
    """
    How often data is being pushed, in seconds.
    """
    events: list[NimbusPushEvent]
    """
    Which events are being pushed.
    """


class NimbusListPushCommandResult(NimbusBaseCommandResult):
    listpush: list[NimbusPushLocation]
    """
    The result of the listpush command.
    """
