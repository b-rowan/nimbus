# Devdetails

## Example
---

### Request
```python exec="on"
from nimbus.requests import NimbusCommandRequest
from pprint import pformat

print("```python")
print(pformat(NimbusCommandRequest(command="devdetails").model_dump(by_alias=True, mode="json", exclude_none=True)))
print("```")
```

### Response
```python exec="on"
from nimbus.examples.handlers import devdetails_handler
from pprint import pformat

print("```python")
print(pformat(devdetails_handler().model_dump(by_alias=True, mode="json")))
print("```")
```

## Response Models
---

::: nimbus.responses.devdetails.NimbusDeviceDetailResult

::: nimbus.responses.devdetails.NimbusDeviceDetailsCommandResult
