import json

from nimbus import __version__
from nimbus.requests import NimbusCommandRequest

EXAMPLE_TAG = "??? example"


def generate_web_examples(command: str, param: dict | None = None) -> str:
    return f"""
{EXAMPLE_TAG} "Example"
    {generate_web_shell_example(command, param)}
    {generate_web_httpx_example(command, param)}
    """


def generate_cgminer_examples(command: str, param: dict | None = None) -> str:
    return f"""
{EXAMPLE_TAG} "Example"
    {generate_cgminer_shell_example(command, param)}
    {generate_cgminer_sockets_example(command, param)}
    """


def generate_web_shell_example(command: str, param: dict | None = None) -> str:
    if param is None:
        return f"""=== "Shell"
        ```shell
        curl http://{{DEVICE_IP}}/nimbus/v{__version__.replace(".", "-")}/{command}
        ```
        """
    else:
        curl_param = json.dumps(param)
        return f"""=== "Shell"
        ```shell
        curl \\
            --request POST \\
            --data {curl_param} \\
            http://{{DEVICE_IP}}/nimbus/v{__version__.replace(".", "-")}/{command}
        ```
        """


def generate_web_httpx_example(command: str, param: dict | None = None):
    if param is None:
        return f"""=== "Python (HTTPX)"
        ```python
        import httpx
        import asyncio

        URL = f"http://{{DEVICE_IP}}/nimbus/v{__version__.replace(".", "-")}/{command}"

        async def main():
            async with httpx.AsyncClient() as c:
                result = await c.get(URL)
            json_data = result.json()
            print(json_data)
            return json_data

        if __name__ == '__main__':
            asyncio.run(main())
        ```
        """
    else:
        return f"""=== "Python (HTTPX)"
        ```python
        import httpx
        import asyncio

        URL = f"http://{{DEVICE_IP}}/nimbus/v{__version__.replace(".", "-")}/{command}"

        async def main():
            async with httpx.AsyncClient() as c:
                result = await c.post(URL, data={param})
            json_data = result.json()
            print(json_data)
            return json_data

        if __name__ == '__main__':
            asyncio.run(main())
        ```
        """


def generate_cgminer_sockets_example(command: str, param: dict | None = None):
    command = NimbusCommandRequest(command=command, param=param)
    return f"""
    === "Python (Sockets)"
        ```python
        import socket
        import json


        def main():
            with socket.create_connection(({{DEVICE_IP}}, 4028)) as sock:
                cmd_str = json.dumps({command.model_dump_json(exclude_none=True)})
                sock.sendall(cmd_str.encode("utf-8"))

                response = b""
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk

            return response.decode("utf-8")


        if __name__ == "__main__":
            response = main()
            print(response)
        ```
    """


def generate_cgminer_shell_example(command: str, param: dict | None = None):
    command = NimbusCommandRequest(command=command, param=param)
    return f"""=== "Shell"
        ```shell
        echo '{command.model_dump_json(exclude_none=True)}' | nc {{DEVICE_IP}} 4028
        ```
    """
