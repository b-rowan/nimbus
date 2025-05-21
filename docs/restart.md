# Restart

Restarting and rebooting are slightly different.
The `restart` command will stop the mining process then start it again.
The `reboot` command is a full device reboot.

See the [reboot](reboot.md) page for more information.

## Example
---

### Request
!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples


    print("Restart now:")
    print("```python")
    print(NimbusCommandRequest(command="restart").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('restart')}")

    print("---")
    print("Wait 10 seconds before restarting:")
    print("```python")
    print(NimbusCommandRequest(command="restart", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(generate_cgminer_examples('restart', param={"after": 10}))
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Restart now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/restart")
    print("```")

    print(f"{generate_web_examples('restart', param={"after": 0})}")

    print("---")
    print("Wait 10 seconds before restarting:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/restart")
    print("```")
    print("Body:")
    print("```")
    print("{\"after\": 10}")
    print("```")

    print(generate_web_examples('restart', param={"after": 10}))
    ```

!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Restart now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/restart")
    print("```")

    print(generate_web_examples('restart'))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import restart_handler
import json

print("```json title='JSON'")
print(json.dumps(restart_handler(param={"after": 10}).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Parameters
---

::: nimbus.requests.restart.NimbusRestartParams

## Response Models
---

::: nimbus.responses.restart.NimbusRestartResult

::: nimbus.responses.restart.NimbusRestartCommandResult
