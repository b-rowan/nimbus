from typing import Any

from nimbus.requests import NimbusCommandRequest


def parse_nimbus_request(command: str, param: Any = None) -> list[NimbusCommandRequest]:
    commands = command.split("+")
    if len(commands) == 1:
        if param is None:
            return [NimbusCommandRequest(command=command, param=param)]
        if param.get(command) is not None:
            return [NimbusCommandRequest(command=command, param=param[command])]
        return [NimbusCommandRequest(command=command, param=param)]
    if isinstance(param, dict):
        return [NimbusCommandRequest(command=c, param=param.get(c)) for c in commands]
    return [NimbusCommandRequest(command=c) for c in commands]
