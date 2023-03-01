from __future__ import annotations
from dataclasses import dataclass, field

from authentication.seedwork.domain.entities import AgregacionRaiz
import authentication.modules.auth.domain.objects_value as ov


@dataclass
class User(AgregacionRaiz):
    id: ov.Id = field(default_factory=ov.Id)
    name: ov.Name = field(default_factory=ov.Name)
    password: ov.Password = field(default_factory=ov.Password)
    role: ov.Role = field(default_factory=ov.Role)

