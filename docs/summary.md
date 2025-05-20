# Summary

## Example
---

### Request
```python exec="on"
from nimbus.requests import NimbusCommandRequest
from pprint import pformat

print("```python")
print(pformat(NimbusCommandRequest(command="summary").model_dump(by_alias=True, mode="json", exclude_none=True)))
print("```")
```

### Response
```python exec="on"
from nimbus.examples.handlers import summary_handler
from pprint import pformat

print("```python")
print(pformat(summary_handler().model_dump(by_alias=True, mode="json")))
print("```")
```


## Response Models:
---

::: nimbus.responses.summary.NimbusSummaryResult

::: nimbus.responses.summary.NimbusMinerMessage

::: nimbus.responses.summary.NimbusMinerMessageSeverity

::: nimbus.responses.summary.NimbusSummaryCommandResult
