from .handlers import handle

try:
    import uvicorn
    from fastapi import APIRouter, FastAPI
except ImportError:
    raise ImportError(
        "Failed to import FastAPI, please run `poetry install --with examples` or install it manually with `pip install fastapi[uvicorn]`"
    )
from nimbus import __version__
from nimbus.util import parse_nimbus_request

router = APIRouter(prefix=f"/nimbus/v{'-'.join(__version__.split('.'))}")


@router.get("/{command}")
async def handle_command(command: str):
    commands = parse_nimbus_request(command)

    if len(commands) == 1:
        return handle(commands[0])
    resp = {c.command: [handle(c)] for c in commands}
    return resp


@router.post("/{command}")
async def handle_command(command: str, param: dict | None = None):
    commands = parse_nimbus_request(command, param)

    if len(commands) == 1:
        return handle(commands[0])
    resp = {c.command: [handle(c)] for c in commands}
    return resp


def run(port: int = 8080):
    app = FastAPI()
    uvicorn.run(app, port=port)


if __name__ == "__main__":
    run()
