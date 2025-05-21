from pydantic import BaseModel


class NimbusRestartParams(BaseModel):
    """
    Restart request parameters.

    Attributes:
        after: How long to wait before restarting mining in seconds.
    """

    after: int | None = None
