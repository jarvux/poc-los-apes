from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Id():
    id: str


@dataclass(frozen=True)
class Name():
    name: str


@dataclass(frozen=True)
class Password():
    password: str


@dataclass(frozen=True)
class Role():
    role: str
