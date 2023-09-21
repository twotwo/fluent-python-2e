from console import tool_poetry


def test_load_toml():
    assert tool_poetry["name"] == "fluent-python-2e"
