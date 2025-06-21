"""
Dictionary helper functions

The pick and omit functions are similar to select-keys and dissoc in Clojure,
and I have borrowed the naming from the JavaScript equivalents in the Lodash.js library.

"""

from typing import Any


def pick(data: dict[Any, Any], keys: set[Any]) -> dict[Any, Any]:
    return {k: v for k, v in data.items() if k in keys}


def omit(data: dict[Any, Any], keys: set[Any]) -> dict[Any, Any]:
    return {k: v for k, v in data.items() if k not in keys}
