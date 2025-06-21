import pytest


@pytest.fixture
# MIT License only for this single function
# Copyright (c) 2025 Yunho Kee
# Copyright (c) 2022 David Vujic
def set_some_environment_variables(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HELLO", "world")


@pytest.fixture
# MIT License only for this single function
# Copyright (c) 2025 Yunho Kee
# Copyright (c) 2022 David Vujic
def fake_data() -> dict[str, str | list[str]]:
    return {"hello": "world", "good": ["morning", "day", "afternoon"]}
