# Pause

## Example
---

### Request
!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples
    from nimbus.requests import NimbusPauseParams


    print("Pause now:")
    print("```python")
    print(NimbusCommandRequest(command="pause").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('pause')}")

    print("---")
    print("Wait 10 seconds before pauseing:")
    print("```python")
    print(NimbusCommandRequest(command="pause", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(generate_cgminer_examples('pause', param={"after": 10}))
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Pause now:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/pause")
    print("```")

    print(f"{generate_web_examples('pause', param={"after": 0})}")

    print("---")
    print("Wait 10 seconds before pauseing:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/pause")
    print("```")
    print("Body:")
    print("```")
    print("{\"after\": 10}")
    print("```")

    print(generate_web_examples('pause', param={"after": 10}))
    ```

!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Pause now:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/pause")
    print("```")

    print(generate_web_examples('pause'))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import pause_handler
from nimbus.requests import NimbusPauseParams
import json

print("```json title='JSON'")
print(json.dumps(pause_handler(param=NimbusPauseParams(after=10)).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Parameters
---

::: nimbus.requests.pause.NimbusPauseParams

## Response Models
---

::: nimbus.responses.pause.NimbusPauseResult

::: nimbus.responses.pause.NimbusPauseCommandResult
