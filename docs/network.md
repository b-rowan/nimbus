# Network

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/network")
    print("```")

    print(f"{generate_web_examples('network')}")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples


    print("```python")
    print(NimbusCommandRequest(command="network").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('network')}")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import network_handler
import json

print("```json title='JSON'")
print(json.dumps(network_handler().model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```

## Response Models
---

::: nimbus.responses.network.NimbusNetworkResult

::: nimbus.responses.network.NimbusNetworkCommandResult
