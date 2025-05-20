from pydantic import BaseModel


class NimbusRebootParams(BaseModel):
    """
    Reboot request parameters.

    Attributes:
        after: How long to wait before rebooting in seconds.
    """

    after: int | None = None
