import json
from datetime import datetime

from nimbus.responses import NimbusNetworkResult

NETWORK = NimbusNetworkResult(
    ip="192.168.1.25", gateway="192.168.1.1", subnet_mask="255.255.255.0", dynamic=True, mac="11:22:33:44:55:66"
)


def test_network_status_schema_validation():
    network = NETWORK

    assert network.ip == "192.168.1.25"
    assert network.mac == "11:22:33:44:55:66"


def test_network_status_schema_serialization():
    network = NETWORK.model_dump(by_alias=True, mode="json")

    assert network["IP"] == "192.168.1.25"
    assert network["MAC"] == "11:22:33:44:55:66"


def test_network_status_schema_json_serialization():
    json.dumps(NETWORK.model_dump(by_alias=True, mode="json"))


def test_network_status_schema_json_validation():
    network = json.loads(NETWORK.model_dump_json(by_alias=True))

    assert network["IP"] == "192.168.1.25"
    assert network["MAC"] == "11:22:33:44:55:66"
