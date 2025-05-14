from datetime import datetime, UTC
from typing import Any

from nimbus.requests import NimbusCommandRequest
from nimbus.responses import *
from nimbus import __version__

MINER = "Nimbus ExampleMiner"
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
                chips=63,
                cores=7182,
                driver=f"nimbus v{__version__}",
                model=MINER,
            )
            for i in range(3)
        ],
    )


CMD_HANDLERS = {
    "version": version_handler,
    "devdetails": devdetails_handler,
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
