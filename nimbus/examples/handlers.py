from datetime import UTC, datetime
from typing import Any

from nimbus import __version__
from nimbus.requests import NimbusCommandRequest
from nimbus.responses import *

MAKE = "Nimbus"
MODEL = "ExampleMiner"
MINER = f"{MAKE} {MODEL}"
CHIPS_PER_BOARD = 63
CORES_PER_CHIP = 114
BOARDS = 3
FANS = 2
COMPILE_TIME = datetime.now(UTC).strftime("%a %b %d %H:%M:%S %Z %Y")


def version_handler(param: Any = None) -> NimbusVersionCommandResult:
    return NimbusVersionCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="version",
                msg=f"nimbus v{__version__}",
            )
        ],
        version=[
            NimbusVersionResult(
                firmware=f"v{__version__}",
                api=f"v{__version__}",
                miner=f"v{__version__}",
                type=MINER,
                compile_time=COMPILE_TIME,
            )
        ],
    )


def devdetails_handler(param: Any = None) -> NimbusDeviceDetailsCommandResult:
    return NimbusDeviceDetailsCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="devdetails",
                msg=f"nimbus v{__version__}",
            )
        ],
        devdetails=[
            NimbusDeviceDetailResult(
                id=i,
                chips=CHIPS_PER_BOARD,
                cores=CHIPS_PER_BOARD * CORES_PER_CHIP,
                driver=f"nimbus v{__version__}",
                model=MINER,
            )
            for i in range(3)
        ],
    )


def hardware_handler(param: Any = None) -> NimbusHardwareCommandResult:
    return NimbusHardwareCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="hardware",
                msg=f"nimbus v{__version__}",
            )
        ],
        hardware=[
            NimbusHardwareResult(
                make=MAKE,
                model=MODEL,
                chips=CHIPS_PER_BOARD * BOARDS,
                cores=CHIPS_PER_BOARD * CORES_PER_CHIP * BOARDS,
                fans=FANS,
                boards=BOARDS,
                board_chips=[CHIPS_PER_BOARD for _ in range(BOARDS)],
                algo="SHA256",
            )
        ],
    )


def summary_handler(param: Any = None) -> NimbusSummaryCommandResult:
    return NimbusSummaryCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="summary",
                msg=f"nimbus v{__version__}",
            )
        ],
        summary=[
            NimbusSummaryResult(
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
                    ),
                    NimbusMinerMessage(
                        when=datetime.now(),
                        message="The device is getting hot. Fans are ramping to 100%.",
                        severity=NimbusMinerMessageSeverity.WARNING,
                    ),
                    NimbusMinerMessage(
                        when=datetime.now(),
                        message="The message system has crashed.",
                        severity=NimbusMinerMessageSeverity.ERROR,
                    ),
                    NimbusMinerMessage(
                        when=datetime.now(),
                        message="The device is currently on fire. Run!",
                        severity=NimbusMinerMessageSeverity.FATAL,
                    ),
                ],
            )
        ],
    )


def pools_handler(param: Any = None):
    return NimbusPoolsCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="pools",
                msg=f"nimbus v{__version__}",
            )
        ],
        pools=[
            NimbusPoolsResult(
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
            ),
            NimbusPoolsResult(
                id=0,
                url="stratum+tcp://solo.nimbus.org:3333",
                group=1,
                status=NimbusPoolStatus.ALIVE,
                priority=0,
                quota=3,
                accepted=100,
                rejected=0,
                stale=0,
                difficulty_accepted=10000,
                difficulty_stale=0,
                difficulty_rejected=0,
                user="NimbusExample.group_1_pool_0",
                stratum_active=True,
            ),
            NimbusPoolsResult(
                id=1,
                url="stratum+tcp://solo.backup.nimbus.org:3333",
                group=1,
                status=NimbusPoolStatus.DEAD,
                priority=1,
                quota=3,
                accepted=0,
                rejected=0,
                stale=0,
                difficulty_accepted=0,
                difficulty_stale=0,
                difficulty_rejected=0,
                user="NimbusExample.group_1_pool_1",
                stratum_active=False,
            ),
        ],
    )


CMD_HANDLERS = {
    "version": version_handler,
    "devdetails": devdetails_handler,
    "hardware": hardware_handler,
    "summary": summary_handler,
    "pools": pools_handler,
}


def handle(command: NimbusCommandRequest):
    if CMD_HANDLERS.get(command.command) is not None:
        return CMD_HANDLERS[command.command](command.param)
    return NimbusBaseCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.WARNING,
                code=-1,
                msg=f"Invalid command: {command.command}",
                description=f"nimbus v{__version__}",
            )
        ]
    )
