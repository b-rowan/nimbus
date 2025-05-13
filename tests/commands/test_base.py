from nimbus import __version__


def test_base_status_schema_validation():
    from nimbus.responses.base import NimbusCommandStatus, NimbusStatusCode

    status = NimbusCommandStatus(
        status=NimbusStatusCode.SUCCESS,
        code=104,
        msg="test_base_status_schema_validation",
        description="cgminer v1.0.0",
    )

    assert status.protocol == f"nimbus v{__version__}"


def test_base_status_schema_serialization():
    from nimbus.responses.base import NimbusCommandStatus, NimbusStatusCode

    status = NimbusCommandStatus(
        status=NimbusStatusCode.SUCCESS,
        code=104,
        msg="test_base_status_schema_serialization",
        description="cgminer v1.0.0",
    ).model_dump(by_alias=True)

    assert status["STATUS"] == NimbusStatusCode.SUCCESS
    assert status["STATUS"] == "S"
    assert status["Code"] == 104
    assert status["Msg"] == "test_base_status_schema_serialization"
    assert status["Protocol"] == f"nimbus v{__version__}"


def test_base_status_schema_json_serialization():
    from nimbus.responses.base import NimbusCommandStatus, NimbusStatusCode
    import json

    json.dumps(
        NimbusCommandStatus(
            status=NimbusStatusCode.SUCCESS,
            code=104,
            msg="test_base_status_schema_serialization",
            description="cgminer v1.0.0",
        ).model_dump(by_alias=True)
    )


def test_base_status_schema_json_validation():
    from nimbus.responses.base import NimbusCommandStatus, NimbusStatusCode
    import json

    status = json.loads(
        json.dumps(
            NimbusCommandStatus(
                status=NimbusStatusCode.SUCCESS,
                code=104,
                msg="test_base_status_schema_serialization",
                description="cgminer v1.0.0",
            ).model_dump(by_alias=True)
        )
    )

    assert status["STATUS"] == NimbusStatusCode.SUCCESS
    assert status["STATUS"] == "S"
    assert status["Code"] == 104
    assert status["Msg"] == "test_base_status_schema_serialization"
    assert status["Protocol"] == f"nimbus v{__version__}"
