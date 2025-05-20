# Version

## Example
---

### Request
!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__

    print("```")
    print(f"/nimbus/v{'-'.join(__version__.split('.'))}/version")
    print("```")
    ```


!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from pprint import pformat


    print("```python")
    print(pformat(NimbusCommandRequest(command="version").model_dump(by_alias=True, mode="json", exclude_none=True)))
    print("```")
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import version_handler
from pprint import pformat

print("```python")
print(pformat(version_handler().model_dump(by_alias=True, mode="json")))
print("```")
```


## Response Models
---

::: nimbus.responses.version.NimbusVersionResult

::: nimbus.responses.version.NimbusVersionCommandResult
