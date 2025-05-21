# Summary

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/summary")
    print("```")

    print(f"{generate_web_examples('summary')}")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples


    print("```python")
    print(NimbusCommandRequest(command="summary").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('summary')}")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import summary_handler
import json

print("```json title='JSON'")
print(json.dumps(summary_handler().model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Response Models
---

::: nimbus.responses.summary.NimbusSummaryResult

::: nimbus.responses.summary.NimbusMinerMessage

::: nimbus.responses.summary.NimbusMinerMessageSeverity

::: nimbus.responses.summary.NimbusSummaryCommandResult
