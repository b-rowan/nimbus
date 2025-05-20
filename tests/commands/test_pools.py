import json

from nimbus.responses.pools import NimbusPoolsResult, NimbusPoolStatus

POOLS = NimbusPoolsResult(
    id=0,
    url="stratum+tcp://pool.nimbus.org:3333",
    group=0,
    status=NimbusPoolStatus.ALIVE,
    priority=0,
    quota=1,
    accepted=100,
    rejected=0,
    stale=0,
    difficulty_accepted=10000,
    difficulty_stale=0,
    difficulty_rejected=0,
    user="NimbusExample.group_0_pool_0",
    stratum_active=True,
)


def test_pools_status_schema_validation():
    pools = POOLS

    assert pools.url == "stratum+tcp://pool.nimbus.org:3333"
    assert pools.user == "NimbusExample.group_0_pool_0"


def test_pools_status_schema_serialization():
    pools = POOLS.model_dump(by_alias=True, mode="json")

    assert pools["URL"] == "stratum+tcp://pool.nimbus.org:3333"
    assert pools["User"] == "NimbusExample.group_0_pool_0"


def test_pools_status_schema_json_serialization():
    json.dumps(POOLS.model_dump(by_alias=True, mode="json"))


def test_pools_status_schema_json_validation():
    pools = json.loads(POOLS.model_dump_json(by_alias=True))

    assert pools["URL"] == "stratum+tcp://pool.nimbus.org:3333"
    assert pools["User"] == "NimbusExample.group_0_pool_0"
