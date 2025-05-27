import asyncio
from contextlib import asynccontextmanager

from nimbus import __version__
from nimbus.examples.rpc import NimbusRPC

try:
    import uvicorn
    from fastapi import FastAPI
except ImportError:
    raise ImportError(
        "Failed to import FastAPI, please run `poetry install --with examples` or install it manually with `pip install fastapi[uvicorn]`"
    )

from nimbus.examples import web


def run(web_port: int = 8080, rpc_port: int = 4028):
    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        rpc_handler = NimbusRPC(port=rpc_port)
        task = asyncio.create_task(rpc_handler.run())
        yield
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None)

    app.mount(f"/nimbus/v{__version__.split('.')[0]}", app=web.router)

    uvicorn.run(app, port=web_port)


if __name__ == "__main__":
    run()
