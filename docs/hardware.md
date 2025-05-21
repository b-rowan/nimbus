# Hardware

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/hardware")
    print("```")

    print(f"{generate_web_examples('hardware')}")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples


    print("```python")
    print(NimbusCommandRequest(command="hardware").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('hardware')}")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import hardware_handler
import json

print("```json title='JSON'")
print(json.dumps(hardware_handler().model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Response Models
---

::: nimbus.responses.hardware.NimbusHardwareResult

::: nimbus.responses.hardware.NimbusHardwareCommandResult
