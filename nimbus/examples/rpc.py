import asyncio
import json

from nimbus import __version__
from nimbus.examples.handlers import handle
from nimbus.requests import parse_nimbus_request
from nimbus.responses import *


class NimbusRPC:
    def __init__(self, address: str = "127.0.0.1", port: int = 4028):
        self.port = port
        self.address = address

    async def run(self):
        server = await asyncio.start_server(self._handle_client, self.address, self.port)
        async with server:
            await server.serve_forever()

    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        raw_data = await reader.read(1000)
        str_data = raw_data.decode()
        try:
            data = json.loads(str_data)
        except json.JSONDecodeError as e:
            writer.write(
                NimbusBaseCommandResult(
                    status=[
                        NimbusCommandStatus(
                            status=NimbusStatusCode.WARNING,
                            code=-1,
                            msg=f"Unable to parse JSON: {e}",
                            description=f"nimbus v{__version__}",
                        )
                    ]
                )
                .model_dump_json(by_alias=True)
                .encode()
            )
            await writer.drain()
            writer.close()
            return

        result = self.handle_command(data)

        writer.write(json.dumps(result).encode())
        await writer.drain()
        writer.close()

    def handle_command(self, command: dict):
        if "cmd" in command:
            cmd = command["cmd"]
        elif "command" in command:
            cmd = command["command"]
        else:
            return NimbusBaseCommandResult(
                status=[
                    NimbusCommandStatus(
                        status=NimbusStatusCode.WARNING,
                        code=-1,
                        msg=f"Could not find command, use the key 'cmd' or 'command'",
                        description=f"nimbus v{__version__}",
                    )
                ]
            ).model_dump(by_alias=True, mode="json")

        commands = parse_nimbus_request(cmd, param=command.get("param"))

        if len(commands) == 1:
            return handle(commands[0]).model_dump(by_alias=True, mode="json")
        resp = {c.command: [handle(c).model_dump(by_alias=True, mode="json")] for c in commands}
        return resp


def run(port: int = 4028):
    rpc = NimbusRPC(port=port)
    rpc.run()


if __name__ == "__main__":
    run()
