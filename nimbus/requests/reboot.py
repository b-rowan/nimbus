from pydantic import BaseModel


class NimbusRebootParams(BaseModel):
    """
    Reboot request parameters.
    """

    after: int | None = None
    """
    How long to wait before rebooting in seconds.
    """
