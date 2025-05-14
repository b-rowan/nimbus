from .handlers import handle

try:
    from fastapi import APIRouter, FastAPI
    import uvicorn
except ImportError:
    raise ImportError(
        "Failed to import FastAPI, please run `poetry install --with examples` or install it manually with `pip install fastapi[uvicorn]`"
    )
from nimbus import __version__
from nimbus.requests import parse_nimbus_request

router = APIRouter(prefix=f"/nimbus/v{'-'.join(__version__.split('.'))}")


@router.get("/{command}")
async def handle_command(command: str):
    commands = parse_nimbus_request(command)

    if len(commands) == 1:
        return handle(commands[0])
    resp = {c.command: [handle(c)] for c in commands}
    return resp


def run(port: int = 8080):
    app = FastAPI()
    uvicorn.run(app, port=port)


if __name__ == "__main__":
    run()
