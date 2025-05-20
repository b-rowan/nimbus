from enum import StrEnum

from pydantic import AliasChoices, BaseModel, ConfigDict, Field, computed_field

from nimbus.responses import NimbusBaseCommandResult


def to_cgminer_key(snake: str):
    return snake.title().replace("_", " ")


class NimbusPoolStatus(StrEnum):
    """
    CGMiner compatible pool status code.

    Attributes:
        ALIVE: The pool is alive and connected.
        DEAD: The pool is disconnected.
        CONNECTING: The device is actively trying to connect to this pool.
        DISABLED: The pool has been disabled by the user.
    """

    ALIVE = "Alive"
    DEAD = "Dead"
    CONNECTING = "Connecting"
    DISABLED = "Disabled"


class NimbusPoolsResult(BaseModel):
    """
    CGMiner compatible pool information.

    Attributes:
        id: The pool ID indexed from 0.
            This must be unique when combined with the value of `group`.
            For example, you may have 2 pools with `id = 0` only if the group id is unique for each.
        url: The full stratum URL for the pool.
            This must be in the correct format for URI parsing.
        group: The group ID for this pool.
        status: The current status of this pool.
        priority: The failover priority for this pool.
            This value should be unique for a given group.
        quota: The quota for this pools group.
            This value may be set to `None` if quotas are unsupported.
            Quota is what portion of mining work should be sent to this group.
            For example, a quota of `1` on group `0` and a quota of `3` on group `1` will result in 75% of work being sent to group `1`.
        accepted: The number of shares the pool has accepted.
        rejected: The number of shares the pool has rejected.
        stale: The number of shares marked as stale.
        difficulty_accepted: The total difficulty of shares the pool has accepted.
        difficulty_rejected: The total difficulty of shares the pool has rejected.
        difficulty_stale: The total difficulty of shares marked as stale.
        user: The pool user for this pool.
        stratum_active: Whether this pool is the current active pool.
        pool: The same value as ID, just included for compatibility.
        alive: Whether the current `status` value is `"Alive"`.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer_key)

    id: int = Field(
        serialization_alias="ID",
        validation_alias=AliasChoices("id", "ID"),
    )
    url: str = Field(
        serialization_alias="URL",
        validation_alias=AliasChoices("url", "URL"),
    )
    group: int = 0
    status: NimbusPoolStatus
    priority: int
    quota: int | None = 0
    accepted: int
    rejected: int
    stale: int
    difficulty_accepted: int
    difficulty_rejected: int
    difficulty_stale: int
    user: str
    stratum_active: bool

    @computed_field(alias="POOL")
    @property
    def pool(self) -> int:
        return self.id

    @computed_field()
    @property
    def alive(self) -> int:
        return self.status == NimbusPoolStatus.ALIVE


class NimbusPoolsCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible pools command result.

    Attributes:
        pools: The result of the pools command, one per pool. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    pools: list[NimbusPoolsResult] = Field(
        serialization_alias="POOLS",
        validation_alias=AliasChoices("pools", "POOLS"),
    )
