from pydantic import BaseModel


class NimbusSetPowerParams(BaseModel):
    """
    Set power request parameters.
    """

    target: int
    """
    The target power, also sometimes called power limit.
    """
