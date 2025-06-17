import asyncio
from datetime import UTC, datetime, timedelta

from pydantic import ValidationError

from nimbus import __version__
from nimbus.extensions import *
from nimbus.requests import *
from nimbus.responses import *

from . import push
from .const import *


def parse_errors(e: ValidationError):
    return ", ".join([f"{error['msg']}: {'>'.join([str(key) for key in error['loc']])}" for error in e.errors()])


def version_handler() -> NimbusVersionCommandResult:
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
                extensions=["tuning.sethashrate", "tuning.setpower"],
            )
        ],
    )


def devdetails_handler() -> NimbusDeviceDetailsCommandResult:
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
                working_chips=CHIPS_PER_BOARD,
                expected_hashrate=4.5,
                serial_number="NIMBOARDTEST123",
                voltage=12.5,
                frequency=400,
                mhs_1m=4.5,
                mhs_5m=4.5,
                mhs_15m=4.5,
                wattage=350,
                wattage_limit=350,
                active=True,
                pcb_temperature=60,
                intake_temperature=65,
                outlet_temperature=85,
                tuned=True,
            )
            for i in range(BOARDS)
        ],
    )


def hardware_handler() -> NimbusHardwareCommandResult:
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


def summary_handler() -> NimbusSummaryCommandResult:
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
                mac=MAC,
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


def pools_handler():
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


def network_handler() -> NimbusNetworkCommandResult:
    return NimbusNetworkCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="network",
                msg=f"nimbus v{__version__}",
            )
        ],
        network=[
            NimbusNetworkResult(
                ip="192.168.1.25",
                gateway="192.168.1.1",
                subnet_mask="255.255.255.0",
                dynamic=True,
                mac=MAC,
            )
        ],
    )


def reboot_handler(param: NimbusRebootParams) -> NimbusRebootCommandResult:
    return NimbusRebootCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="reboot",
                msg=f"nimbus v{__version__}",
            )
        ],
        reboot=[NimbusRebootResult(when=datetime.now(UTC) + timedelta(seconds=param.after or 0))],
    )


def restart_handler(param: NimbusRestartParams) -> NimbusRestartCommandResult:
    return NimbusRestartCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="restart",
                msg=f"nimbus v{__version__}",
            )
        ],
        restart=[NimbusRestartResult(when=datetime.now(UTC) + timedelta(seconds=param.after or 0))],
    )


def setpools_handler(param: NimbusSetPoolsParams) -> NimbusSetPoolsCommandResult:
    return NimbusSetPoolsCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="setpools",
                msg=f"nimbus v{__version__}",
            )
        ],
        setpools=[
            NimbusSetPoolsResult(
                groups=len(param.groups),
                pools=len([pool for group in param.groups for pool in group.pools]),
            )
        ],
    )


def setpower_handler(param: NimbusSetPowerParams) -> NimbusSetPowerCommandResult:
    return NimbusSetPowerCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="setpower",
                msg=f"nimbus v{__version__}",
            )
        ],
        setpower=[NimbusSetPowerResult(target=param.target)],
    )


def sethashrate_handler(param: NimbusSetHashrateParams) -> NimbusSetHashrateCommandResult:
    return NimbusSetHashrateCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="sethashrate",
                msg=f"nimbus v{__version__}",
            )
        ],
        sethashrate=[NimbusSetHashrateResult(target=param.target)],
    )


def listpush_handler() -> NimbusListPushCommandResult:
    return NimbusListPushCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.INFO,
                description="listpush",
                msg=f"nimbus v{__version__}",
            )
        ],
        listpush=push.handler.pusher_list,
    )


def addpush_handler(param: NimbusAddPushParams) -> NimbusAddPushCommandResult:
    push.handler.add_push(NimbusPushLocation.model_validate(param))

    return NimbusAddPushCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="addpush",
                msg=f"nimbus v{__version__}",
            )
        ],
        addpush=[NimbusAddPushResult(name=param.name)],
    )


def delpush_handler(param: NimbusDeletePushParams) -> NimbusDeletePushCommandResult:
    asyncio.create_task(push.handler.remove_push(param.name))

    return NimbusDeletePushCommandResult(
        status=[
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                description="delpush",
                msg=f"nimbus v{__version__}",
            )
        ],
        delpush=[NimbusDeletePushResult(name=param.name)],
    )


CMD_HANDLERS = {
    "version": version_handler,
    "devdetails": devdetails_handler,
    "hardware": hardware_handler,
    "summary": summary_handler,
    "pools": pools_handler,
    "network": network_handler,
    "reboot": reboot_handler,
    "listpush": listpush_handler,
    "setpools": setpools_handler,
    "setpower": setpower_handler,
    "sethashrate": sethashrate_handler,
    "addpush": addpush_handler,
    "delpush": delpush_handler,
}


def handle(command: NimbusCommandRequest):
    if CMD_HANDLERS.get(command.command) is not None:
        if command.param is not None:
            return CMD_HANDLERS[command.command](command.param)
        return CMD_HANDLERS[command.command]()
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
