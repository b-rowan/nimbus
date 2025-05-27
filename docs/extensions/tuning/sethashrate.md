# Set Hashrate (Tuning)

## Example
---

!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples

    param = {
        "target": 15,
    }

    print("```python")
    print(NimbusCommandRequest(command="sethashrate", param=param).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('sethashrate', param=param)}")
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples
    import json

    param = {
        "target": 15,
    }

    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/sethashrate")
    print("```")
    print("Body:")
    print("```JSON")
    print(json.dumps(param))
    print("```")

    print(generate_web_examples('sethashrate', param=param))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import sethashrate_handler
from nimbus.extensions.requests import NimbusSetPowerParams
import json

param = NimbusSetPowerParams(target=15)

print("```json title='JSON'")
print(json.dumps(sethashrate_handler(param=param).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```

## Parameters
---

::: nimbus.extensions.requests.tuning.NimbusSetPowerParams

## Response Models
---

::: nimbus.extensions.responses.tuning.NimbusSetPowerResult

::: nimbus.extensions.responses.tuning.NimbusSetPowerCommandResult
