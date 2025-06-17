from pydantic import BaseModel


class NimbusDeletePushParams(BaseModel):
    """
    Delete push request parameters.
    """

    name: str
    """
    The name of the push location to delete.
    """
