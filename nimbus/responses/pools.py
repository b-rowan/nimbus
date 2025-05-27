from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, computed_field

from nimbus.responses import NimbusBaseCommandResult
from nimbus.util.serialize import to_cgminer


class NimbusPoolStatus(StrEnum):
    """
    CGMiner compatible pool status code.
    """

    ALIVE = "Alive"
    """
    The pool is alive and connected.
    """
    DEAD = "Dead"
    """
    The pool is disconnected.
    """
    CONNECTING = "Connecting"
    """
    The device is actively trying to connect to this pool.
    """
    DISABLED = "Disabled"
    """
    The pool has been disabled by the user.
    """


class NimbusPoolsResult(BaseModel):
    """
    CGMiner compatible pool information.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    id: int = Field(alias="ID", title="ID")
    """
    The pool ID indexed from 0.
    This must be unique when combined with the value of `group`.
    For example, you may have 2 pools with `id = 0` only if the group id is unique for each.
    """
    url: str = Field(alias="URL", title="URL")
    """
    The full stratum URL for the pool.
    This must be in the correct format for URI parsing.
    """
    group: int = 0
    """
    The group ID for this pool.
    """
    status: NimbusPoolStatus
    """
    The current status of this pool.
    """
    priority: int
    """
    The failover priority for this pool.
    This value should be unique for a given group.
    """
    quota: int | None = 0
    """
    The quota for this pools group.
    This value may be set to `None` if quotas are unsupported.
    Quota is what portion of mining work should be sent to this group.
    For example, a quota of `1` on group `0` and a quota of `3` on group `1` will result in 75% of work being sent to group `1`.
    """
    accepted: int
    """
    The number of shares the pool has accepted.
    """
    rejected: int
    """
    The number of shares the pool has rejected.
    """
    stale: int
    """
    The number of shares marked as stale.
    """
    difficulty_accepted: int
    """
    The total difficulty of shares the pool has accepted.
    """
    difficulty_rejected: int
    """
    The total difficulty of shares the pool has rejected.
    """
    difficulty_stale: int
    """
    The total difficulty of shares marked as stale.
    """
    user: str
    """
    The pool user for this pool.
    """
    stratum_active: bool
    """
    Whether this pool is the current active pool.
    """

    @computed_field(alias="POOL")
    @property
    def pool(self) -> int:
        """
        The same value as ID, just included for CGMiner compatibility.
        """
        return self.id

    @computed_field()
    @property
    def alive(self) -> int:
        """
        Whether the current `status` value is `"Alive"`.
        """
        return self.status == NimbusPoolStatus.ALIVE


class NimbusPoolsCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible pools command result.
    """

    pools: list[NimbusPoolsResult]
    """
    The result of the pools command, one per pool. CGMiner compatible.
    """
