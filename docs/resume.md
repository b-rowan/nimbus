# Resume

## Example
---

### Request
!!! cgminer "CGMiner style command"
    ```python exec="on"
    from nimbus.requests import NimbusCommandRequest
    from nimbus.docs import generate_cgminer_examples
    from nimbus.requests import NimbusResumeParams


    print("Resume now:")
    print("```python")
    print(NimbusCommandRequest(command="resume").model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(f"{generate_cgminer_examples('resume')}")

    print("---")
    print("Wait 10 seconds before resumeing:")
    print("```python")
    print(NimbusCommandRequest(command="resume", param={"after": 10}).model_dump(by_alias=True, mode="json", exclude_none=True))
    print("```")

    print(generate_cgminer_examples('resume', param={"after": 10}))
    ```

!!! post-request "POST request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Resume now:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/resume")
    print("```")

    print(f"{generate_web_examples('resume', param={"after": 0})}")

    print("---")
    print("Wait 10 seconds before resumeing:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/resume")
    print("```")
    print("Body:")
    print("```")
    print("{\"after\": 10}")
    print("```")

    print(generate_web_examples('resume', param={"after": 10}))
    ```

!!! get-request "GET request"
    ```python exec="on"
    from nimbus import __version__
    from nimbus.docs import generate_web_examples

    print("Resume now:")
    print("```")
    print(f"/nimbus/v{__version__.split('.')[0]}/resume")
    print("```")

    print(generate_web_examples('resume'))
    ```

### Response
```python exec="on"
from nimbus.examples.handlers import resume_handler
from nimbus.requests import NimbusResumeParams
import json

print("```json title='JSON'")
print(json.dumps(resume_handler(param=NimbusResumeParams(after=10)).model_dump(by_alias=True, mode="json"), indent=4))
print("```")
```


## Parameters
---

::: nimbus.requests.resume.NimbusResumeParams

## Response Models
---

::: nimbus.responses.resume.NimbusResumeResult

::: nimbus.responses.resume.NimbusResumeCommandResult
