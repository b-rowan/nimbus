from pydantic import BaseModel


class NimbusSetHashrateParams(BaseModel):
    """
    Set hashrate request parameters.
    """

    target: int
    """
    The target hashrate.
    """
