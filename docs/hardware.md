# Hardware

## Example
---

### Request
```python exec="on"
from nimbus.requests import NimbusCommandRequest
from pprint import pformat

print("```python")
print(pformat(NimbusCommandRequest(command="hardware").model_dump(by_alias=True, mode="json", exclude_none=True)))
print("```")
```

### Response
```python exec="on"
from nimbus.examples.handlers import hardware_handler
from pprint import pformat

print("```python")
print(pformat(hardware_handler().model_dump(by_alias=True, mode="json")))
print("```")
```


## Response Models:
---

::: nimbus.responses.hardware.NimbusHardwareResult

::: nimbus.responses.hardware.NimbusHardwareCommandResult
