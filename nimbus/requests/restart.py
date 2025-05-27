from pydantic import BaseModel


class NimbusRestartParams(BaseModel):
    """
    Restart request parameters.
    """

    after: int | None = None
    """
    How long to wait before restarting mining in seconds.
    """
