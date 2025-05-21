# Devdetails

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/devdetails")
    print("```")

    print(f"{generate_web_examples('devdetails')}")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from pprint import pformat
    from nimbus.docs import generate_cgminer_examples


    print("```python")
    print(NimbusCommandRequest(command="devdetails").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('devdetails')}")
    ```



### Response
```python exec="on"
from nimbus.examples.handlers import devdetails_handler
import json

print("```json title='JSON'")
print(json.dumps(devdetails_handler().model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```

## Response Models
---

::: nimbus.responses.devdetails.NimbusDeviceDetailResult

::: nimbus.responses.devdetails.NimbusDeviceDetailsCommandResult
