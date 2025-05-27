from pydantic import BaseModel


class NimbusSetPoolsPool(BaseModel):
    """
    Set pools pool.

    Represents a single pool.
    """

    url: str
    """
    The URL for this pool.
    """
    user: str
    """
    The username and worker name to be used on the pool.
    """
    password: str
    """
    The password to use for this pool.
    """


class NimbusSetPoolsPoolGroup(BaseModel):
    """
    Set pools pool group.

    Represents a group of pools with a shared quota.
    """

    name: str | None = None
    """
    The name of this pool group.
    This may or may not be used on the device side, but to ensure compatibility with all systems it is included.
    """
    quota: int = 1
    """
    The quota for this pool group.
    Shares are distributed by totaling all group quotas, then taking the current group quota divided by total quota.
    """
    pools: list[NimbusSetPoolsPool]
    """
    The pools for this pool group.
    """


class NimbusSetPoolsParams(BaseModel):
    """
    Set pools request parameters.
    """

    groups: list[NimbusSetPoolsPoolGroup]
    """
    A list of pool groups to be set on the device.
    """
