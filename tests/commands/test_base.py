import json

from nimbus import __version__
from nimbus.responses import NimbusCommandStatus, NimbusStatusCode

STATUS = NimbusCommandStatus(
    status=NimbusStatusCode.SUCCESS,
    code=104,
    msg="test_base_status_schema_validation",
    description="cgminer v1.0.0",
)


def test_base_status_schema_validation():
    status = STATUS

    assert status.protocol == f"nimbus v{__version__}"


def test_base_status_schema_serialization():
    status = STATUS.model_dump(by_alias=True, mode="json")

    assert status["STATUS"] == "S"
    assert status["Code"] == 104
    assert status["Msg"] == "test_base_status_schema_serialization"
    assert status["Protocol"] == f"nimbus v{__version__}"


def test_base_status_schema_json_serialization():
    json.dumps(STATUS.model_dump(by_alias=True, mode="json"))


def test_base_status_schema_json_validation():
    status = json.loads(STATUS.model_dump_json(by_alias=True))

    assert status["STATUS"] == "S"
    assert status["Code"] == 104
    assert status["Msg"] == "test_base_status_schema_serialization"
    assert status["Protocol"] == f"nimbus v{__version__}"
