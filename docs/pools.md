# Pools

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/pools")
    print("```")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from pprint import pformat


    print("```python")
    print(pformat(NimbusCommandRequest(command="pools").model_dump(by_alias=True, mode="json", exclude_none=True)))
    print("```")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import pools_handler
from pprint import pformat

print("```python")
print(pformat(pools_handler().model_dump(by_alias=True, mode="json")))
print("```")
```


## Response Models
---

::: nimbus.responses.pools.NimbusPoolsResult

::: nimbus.responses.pools.NimbusPoolStatus

::: nimbus.responses.pools.NimbusPoolsCommandResult
