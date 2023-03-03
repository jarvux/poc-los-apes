from dataclasses import dataclass, field
from .mixins import ValidarReglasMixin
from .rules import IdEntidadEsInmutable
from .exceptions import IdDebeSerInmutableExcepcion
import uuid

@dataclass
class Entidad:
    id: str = field(default=str)
    _id: str = field(init=False, repr=False)
    name: str =  field(default=str)
    password: str =  field(default=str)
    role: int =  field(default=int)
    
   
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: str) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.siguiente_id()
        