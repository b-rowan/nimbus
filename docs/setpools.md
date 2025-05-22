# Set Pools

## Example
---

!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples

    param = {
        "groups": [{"name": "Test",
            "pools": [{"url": "stratum+tcp://stratum.slushpool.com:3333", "user": "test", "password": "123"}]
        }]
    }

    print("```python")
    print(NimbusCommandRequest(command="setpools", param=param).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('setpools', param=param)}")
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples
    import json

    param = {
        "groups": [{"name": "Test",
            "pools": [{"url": "stratum+tcp://stratum.slushpool.com:3333", "user": "test", "password": "123"}]
        }]
    }

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/setpools")
    print("```")
    print("Body:")
    print("```")
    print(json.dumps(param))
    print("```")

    print(generate_web_examples('setpools', param=param))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import setpools_handler
import json

param = {
    "groups": [{"name": "Test",
        "pools": [{"url": "stratum+tcp://stratum.slushpool.com:3333", "user": "test", "password": "123"}]
    }]
}

print("```json title='JSON'")
print(json.dumps(setpools_handler(param=param).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```

## Parameters
---

::: nimbus.requests.setpools.NimbusSetPoolsParams

::: nimbus.requests.setpools.NimbusSetPoolsPoolGroup

::: nimbus.requests.setpools.NimbusSetPoolsPool


## Response Models
---

::: nimbus.responses.setpools.NimbusSetPoolsResult

::: nimbus.responses.setpools.NimbusSetPoolsCommandResult
