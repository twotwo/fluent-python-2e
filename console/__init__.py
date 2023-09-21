import toml  # type:ignore

tool_poetry = toml.load("pyproject.toml")["tool"]["poetry"]


def run():
    """This is the main entrypoint to your application"""
    print(f"This is {tool_poetry['name']}. Let's build some cool python apps!")
