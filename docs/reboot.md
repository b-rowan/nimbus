# Reboot

## Example
---

### Request
!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples


    print("Reboot now:")
    print("```python")
    print(NimbusCommandRequest(command="reboot").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('reboot')}")

    print("---")
    print("Wait 10 seconds before rebooting:")
    print("```python")
    print(NimbusCommandRequest(command="reboot", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(generate_cgminer_examples('reboot', param={"after": 10}))
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Reboot now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")

    print(f"{generate_web_examples('reboot', param={"after": 0})}")

    print("---")
    print("Wait 10 seconds before rebooting:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")
    print("Body:")
    print("```")
    print("{\"after\": 10}")
    print("```")

    print(generate_web_examples('reboot', param={"after": 10}))
    ```

!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Reboot now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")

    print(generate_web_examples('reboot'))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import reboot_handler
import json

print("```json title='JSON'")
print(json.dumps(reboot_handler(param={"after": 10}).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Parameters
---

::: nimbus.requests.reboot.NimbusRebootParams

## Response Models
---

::: nimbus.responses.reboot.NimbusRebootResult

::: nimbus.responses.reboot.NimbusRebootCommandResult
