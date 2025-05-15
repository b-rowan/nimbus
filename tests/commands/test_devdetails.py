from nimbus import __version__
from nimbus.responses.devdetails import NimbusDeviceDetailResult
import json

MINER = "Nimbus ExampleMiner"
DEVDETAILS = NimbusDeviceDetailResult(
    id=0,
    chips=63,
    cores=7182,
    driver=f"nimbus v{__version__}",
    model=MINER,
)


def test_devdetails_status_schema_validation():
    devdetails = DEVDETAILS

    assert devdetails.driver == f"nimbus v{__version__}"


def test_devdetails_status_schema_serialization():
    devdetails = DEVDETAILS.model_dump(by_alias=True, mode="json")

    assert devdetails["ID"] == 0
    assert devdetails["Chips"] == 63
    assert devdetails["Cores"] == 7182
    assert devdetails["Driver"] == f"nimbus v{__version__}"
    assert devdetails["Model"] == MINER


def test_devdetails_status_schema_json_serialization():
    json.dumps(DEVDETAILS.model_dump(by_alias=True, mode="json"))


def test_devdetails_status_schema_json_validation():
    devdetails = json.loads(DEVDETAILS.model_dump_json(by_alias=True))

    assert devdetails["ID"] == 0
    assert devdetails["Chips"] == 63
    assert devdetails["Cores"] == 7182
    assert devdetails["Driver"] == f"nimbus v{__version__}"
    assert devdetails["Model"] == MINER
