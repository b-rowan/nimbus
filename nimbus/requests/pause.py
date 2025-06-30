from pydantic import BaseModel


class NimbusPauseParams(BaseModel):
    """
    Pause request parameters.
    """

    after: int | None = None
    """
    How long to wait before pausing mining in seconds.
    """
