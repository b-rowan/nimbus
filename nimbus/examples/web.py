from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .handlers import *

try:
    import uvicorn
    from fastapi import APIRouter, FastAPI
except ImportError:
    raise ImportError(
        "Failed to import FastAPI, please run `poetry install --with examples` or install it manually with `pip install fastapi[uvicorn]`"
    )
from nimbus import __version__
from nimbus.util import parse_nimbus_request

router = FastAPI(responses={422: {"model": NimbusBaseCommandResult}})


@router.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, e: RequestValidationError):
    return JSONResponse(
        NimbusBaseCommandResult(
            status=[
                NimbusCommandStatus(
                    status=NimbusStatusCode.ERROR,
                    code=-1,
                    msg=parse_errors(e),
                    description=f"nimbus v{__version__}",
                )
            ]
        ).model_dump(mode="json"),
        status_code=422,
    )


@router.get("/version")
async def command_version() -> NimbusVersionCommandResult:
    return version_handler()


@router.get("/devdetails")
async def command_devdetails() -> NimbusDeviceDetailsCommandResult:
    return devdetails_handler()


@router.get("/hardware")
async def command_hardware() -> NimbusHardwareCommandResult:
    return hardware_handler()


@router.get("/summary")
async def command_summary() -> NimbusSummaryCommandResult:
    return summary_handler()


@router.get("/pools")
async def command_pools() -> NimbusPoolsCommandResult:
    return pools_handler()


@router.get("/listpush")
async def command_listpush() -> NimbusListPushCommandResult:
    return listpush_handler()


@router.get("/network")
async def command_network() -> NimbusNetworkCommandResult:
    return network_handler()


@router.get("/reboot")
async def command_reboot() -> NimbusRebootCommandResult:
    return reboot_handler(NimbusRebootParams())


@router.post("/reboot")
async def command_reboot(param: NimbusRebootParams) -> NimbusRebootCommandResult:
    return reboot_handler(param)


@router.get("/restart")
async def command_restart() -> NimbusRestartCommandResult:
    return restart_handler(NimbusRestartParams())


@router.post("/restart")
async def command_restart(param: NimbusRestartParams) -> NimbusRestartCommandResult:
    return restart_handler(param)


@router.post("/setpools")
async def command_setpools(param: NimbusSetPoolsParams) -> NimbusSetPoolsCommandResult | NimbusBaseCommandResult:
    return setpools_handler(param)


@router.post("/setpower")
async def command_setpower(param: NimbusSetPowerParams) -> NimbusSetPowerCommandResult | NimbusBaseCommandResult:
    return setpower_handler(param)


@router.post("/addpush")
async def command_addpush(param: NimbusAddPushParams) -> NimbusAddPushCommandResult | NimbusBaseCommandResult:
    return addpush_handler(param)


@router.get("/{multicommand}")
async def handle_multicommand(command: str):
    commands = parse_nimbus_request(command)

    if len(commands) == 1:
        return handle(commands[0])
    resp = {c.command: [handle(c)] for c in commands}
    return resp


@router.post("/{multicommand}")
async def handle_multicommand(multicommand: str, param: dict | None = None):
    commands = parse_nimbus_request(multicommand, param)

    if len(commands) == 1:
        return handle(commands[0])
    resp = {c.command: [handle(c)] for c in commands}
    return resp


def run(port: int = 8080):
    app = FastAPI()
    uvicorn.run(app, port=port)


if __name__ == "__main__":
    run()
