import typing
from collections import defaultdict


class FixedKeyDict(defaultdict):
    def __init__(self, *keys: typing.Hashable, default_value=""):
        self._keys = frozenset(keys)
        super().__init__(lambda: default_value)

    def __getitem__(self, key):
        if key not in self._keys:
            raise KeyError(f"Invalid key '{key}'. Set key when creating FixedKeyDict.")

        return super().__getitem__(key)

    def __setitem__(self, key, val):
        if key not in self._keys:
            raise KeyError(f"Invalid key '{key}'. Set key when creating FixedKeyDict.")

        super().__setitem__(key, val)
