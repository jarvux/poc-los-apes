from dataclasses import dataclass, field
from .mixins import ValidarReglasMixin
from .rules import IdEntidadEsInmutable
from .exceptions import IdDebeSerInmutableExcepcion
import uuid

@dataclass
class Entidad:
    id:  uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    name: str = field(default=str)
    password: str = field(default=str)
    role: str = field(default=str)

    @classmethod
    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.next_id()

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    ...