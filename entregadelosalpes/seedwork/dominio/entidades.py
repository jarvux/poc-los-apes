from dataclasses import dataclass, field
from datetime import datetime
from .eventos import EventoDominio 
import uuid
from pydispatch import dispatcher
        
@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: str = field(default=str)
    fecha_actualizacion: str = field(default=str)

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        self._id = self.siguiente_id()

@dataclass
class AgregacionRaiz(Entidad):
    eventos: list[EventoDominio] = field(default_factory=list)

    def agregar_evento(self, evento: EventoDominio):
        self.eventos.append(evento)
        dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)

    def limpiar_eventos(self):
        self.eventos = list()



    
