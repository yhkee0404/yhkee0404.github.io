from development.ci.utils import hello

from yhkee0404.example_dictionaries.core import omit, pick


def test_pick(fake_data: dict[str, str | list[str]]):
    assert pick(fake_data, {"good"}) == {"good": ["morning", "day", "afternoon"]}


def test_omit(fake_data: dict[str, str | list[str]]):
    assert omit(fake_data, {"good"}) == {"hello": "world"}


def test_environment_customization(set_some_environment_variables: None):
    import os

    data = os.getenv("HELLO")

    assert data == "world"


def test_shared_code():
    assert hello() == "world"
