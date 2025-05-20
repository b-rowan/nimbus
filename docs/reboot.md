# Reboot

## Example
---

### Request
```python exec="on"
from nimbus.requests import NimbusCommandRequest
from pprint import pformat

print("Reboot now:")
print("```python")
print(pformat(NimbusCommandRequest(command="reboot").model_dump(by_alias=True, mode="json", exclude_none=True)))
print("```")

print("Wait 10 seconds before rebooting:")
print("```python")
print(pformat(NimbusCommandRequest(command="reboot", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True)))
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


## Parameters:
---

::: nimbus.requests.reboot.NimbusRebootParams

## Response Models:
---

::: nimbus.responses.reboot.NimbusRebootResult

::: nimbus.responses.reboot.NimbusRebootCommandResult
