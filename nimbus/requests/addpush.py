import random
import string

from pydantic import AnyHttpUrl, BaseModel, Field

from nimbus.push.base import NimbusPushEvent

random_name = lambda: "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


class NimbusAddPushParams(BaseModel):
    """
    Add push request parameters.
    """

    name: str = Field(default_factory=random_name)
    """
    The name of the push location.
    Randomly generated if not set.
    """
    endpoint: AnyHttpUrl
    """
    The web endpoint to push data to.
    Data is sent via a POST request.
    """
    frequency: int
    """
    How often to push data, in seconds.
    """
    events: list[NimbusPushEvent] = Field(default_factory=lambda: list(NimbusPushEvent))
    """
    Which events to subscribe to.
    Defaults to all.
    """
