from nimbus import __version__


def test_base_status_schema_validation():
    from nimbus.responses.version import NimbusVersionResult

    version = NimbusVersionResult(
        firmware="v1.0.0",
        miner="v1.0.0",
        compile_time="Tue May 13 14:56:45 CST 2025",
        type="Antminer S9",
    )

    assert version.api == f"v{__version__}"


def test_base_status_schema_serialization():
    from nimbus.responses.version import NimbusVersionResult

    version = NimbusVersionResult(
        firmware="v1.0.0",
        miner="v1.0.0",
        compile_time="Tue May 13 14:56:45 CST 2025",
        type="Antminer S9",
    ).model_dump(by_alias=True)

    assert version["Firmware"] == "v1.0.0"
    assert version["API"] == f"v{__version__}"
    assert version["Miner"] == "v1.0.0"
    assert version["CompileTime"] == "Tue May 13 14:56:45 CST 2025"
    assert version["Type"] == "Antminer S9"


def test_base_status_schema_json_serialization():
    from nimbus.responses.version import NimbusVersionResult
    import json

    json.dumps(
        NimbusVersionResult(
            firmware="v1.0.0",
            miner="v1.0.0",
            compile_time="Tue May 13 14:56:45 CST 2025",
            type="Antminer S9",
        ).model_dump(by_alias=True)
    )


def test_base_status_schema_json_validation():
    from nimbus.responses.version import NimbusVersionResult
    import json

    version = json.loads(
        json.dumps(
            NimbusVersionResult(
                firmware="v1.0.0",
                miner="v1.0.0",
                compile_time="Tue May 13 14:56:45 CST 2025",
                type="Antminer S9",
            ).model_dump(by_alias=True)
        )
    )

    assert version["Firmware"] == "v1.0.0"
    assert version["API"] == f"v{__version__}"
    assert version["Miner"] == "v1.0.0"
    assert version["CompileTime"] == "Tue May 13 14:56:45 CST 2025"
    assert version["Type"] == "Antminer S9"
