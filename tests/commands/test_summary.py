import json
from datetime import datetime

from nimbus.responses.common import NimbusMinerMessage, NimbusMinerMessageSeverity
from nimbus.responses.summary import NimbusSummaryResult

SUMMARY = NimbusSummaryResult(
    elapsed=100,
    uptime=100,
    mhs_avg=13500000,
    mhs_1m=13500000,
    mhs_5m=13500000,
    mhs_15m=13500000,
    mac="11:22:33:44:55:66",
    serial_number="NIM123456TEST",
    control_board="NimBoard",
    fans=[6000, 6000],
    fan_speed=100,
    psu_fans=[],
    psu_fan_speed=100,
    chip_temperature_avg=70,
    board_temperature_avg=55,
    fluid_temperature=25,
    wattage=1400,
    wattage_limit=1420,
    is_mining=True,
    messages=[
        NimbusMinerMessage(
            when=datetime.now(),
            message="Testing the message system.",
            severity=NimbusMinerMessageSeverity.INFO,
        )
    ],
)


def test_summary_status_schema_validation():
    summary = SUMMARY

    assert summary.serial_number == "NIM123456TEST"
    assert summary.mac == "11:22:33:44:55:66"


def test_summary_status_schema_serialization():
    summary = SUMMARY.model_dump(by_alias=True, mode="json")

    assert summary["Serial Number"] == "NIM123456TEST"
    assert summary["MAC"] == "11:22:33:44:55:66"


def test_summary_status_schema_json_serialization():
    json.dumps(SUMMARY.model_dump(by_alias=True, mode="json"))


def test_summary_status_schema_json_validation():
    summary = json.loads(SUMMARY.model_dump_json(by_alias=True))

    assert summary["Serial Number"] == "NIM123456TEST"
    assert summary["MAC"] == "11:22:33:44:55:66"
