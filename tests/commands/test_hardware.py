import json

from nimbus.responses.hardware import NimbusHardwareResult

MAKE = "Nimbus"
MODEL = "ExampleMiner"
HARDWARE = NimbusHardwareResult(
    make=MAKE,
    model=MODEL,
    chips=189,
    cores=21546,
    boards=3,
    fans=2,
    board_chips=[63, 63, 63],
    algo="SHA256",
)


def test_hardware_status_schema_validation():
    hardware = HARDWARE

    assert hardware.make == MAKE
    assert hardware.model == MODEL


def test_hardware_status_schema_serialization():
    hardware = HARDWARE.model_dump(by_alias=True, mode="json")

    assert hardware["Make"] == MAKE
    assert hardware["Model"] == MODEL
    assert hardware["Chips"] == 189
    assert hardware["Cores"] == 21546
    assert hardware["Fans"] == 2
    assert hardware["Board Chips"] == [63, 63, 63]
    assert hardware["Algo"] == "SHA256"


def test_hardware_status_schema_json_serialization():
    json.dumps(HARDWARE.model_dump(by_alias=True, mode="json"))


def test_hardware_status_schema_json_validation():
    hardware = json.loads(HARDWARE.model_dump_json(by_alias=True))

    assert hardware["Make"] == MAKE
    assert hardware["Model"] == MODEL
    assert hardware["Chips"] == 189
    assert hardware["Cores"] == 21546
    assert hardware["Fans"] == 2
    assert hardware["Board Chips"] == [63, 63, 63]
    assert hardware["Algo"] == "SHA256"
