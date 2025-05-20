from pydantic import AliasChoices, BaseModel, Field


class NimbusCommandRequest(BaseModel):
    command: str = Field(
        validation_alias=AliasChoices("cmd", "command"),
    )
    param: dict | None = None
