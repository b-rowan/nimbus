import json

from nimbus import __version__
from nimbus.responses.devdetails import NimbusDeviceDetailResult

MINER = "Nimbus ExampleMiner"
DEVDETAILS = NimbusDeviceDetailResult(
    id=0,
    chips=63,
    cores=7182,
    driver=f"nimbus v{__version__}",
    model=MINER,
    working_chips=63,
    expected_hashrate=4.5,
    serial_number="NIMBOARDTEST123",
    voltage=12.5,
    frequency=400,
    mhs_1m=4.5,
    mhs_5m=4.5,
    mhs_15m=4.5,
    active=True,
    pcb_temperature=60,
    intake_temperature=65,
    outlet_temperature=85,
    tuned=True,
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
