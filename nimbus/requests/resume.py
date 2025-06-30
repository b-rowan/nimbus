from pydantic import BaseModel


class NimbusResumeParams(BaseModel):
    """
    Resume request parameters.
    """

    after: int | None = None
    """
    How long to wait before resuming mining in seconds.
    """
