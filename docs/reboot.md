# Reboot

## Example
---

### Request
!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from pprint import pformat

    print("Reboot now:")
    print("```python")
    print(pformat(NimbusCommandRequest(command="reboot").model_dump(by_alias=True, mode="json", exclude_none=True)))
    print("```")
    print("---")
    print("Wait 10 seconds before rebooting:")
    print("```python")
    print(pformat(NimbusCommandRequest(command="reboot", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True)))
    print("```")
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from pprint import pformat

    print("Reboot now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")
    print("---")
    print("Wait 10 seconds before rebooting:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")
    print("Body:")
    print("```")
    print("{\"after\": 10}")
    print("```")
    ```

!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from pprint import pformat

    print("Reboot now:")
    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/reboot")
    print("```")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import reboot_handler
from pprint import pformat

print("```python")
print(pformat(reboot_handler(param={"after": 10}).model_dump(by_alias=True, mode="json")))
print("```")
```


## Parameters
---

::: nimbus.requests.reboot.NimbusRebootParams

## Response Models
---

::: nimbus.responses.reboot.NimbusRebootResult

::: nimbus.responses.reboot.NimbusRebootCommandResult
