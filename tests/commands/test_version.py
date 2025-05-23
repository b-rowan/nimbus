import json

from nimbus import __version__
from nimbus.responses.version import NimbusVersionResult

VERSION = NimbusVersionResult(
    firmware="v1.0.0",
    miner="v1.0.0",
    type="Antminer S9",
)


def test_version_status_schema_validation():
    version = VERSION

    assert version.api == f"v{__version__}"


def test_version_status_schema_serialization():
    version = VERSION.model_dump(by_alias=True, mode="json")

    assert version["Firmware"] == "v1.0.0"
    assert version["API"] == f"v{__version__}"
    assert version["Miner"] == "v1.0.0"
    assert version["Type"] == "Antminer S9"


def test_version_status_schema_json_serialization():
    json.dumps(VERSION.model_dump(by_alias=True, mode="json"))


def test_version_status_schema_json_validation():
    version = json.loads(VERSION.model_dump_json(by_alias=True))

    assert version["Firmware"] == "v1.0.0"
    assert version["API"] == f"v{__version__}"
    assert version["Miner"] == "v1.0.0"
    assert version["Type"] == "Antminer S9"
