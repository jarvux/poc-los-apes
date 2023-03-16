import pickle
from dataclasses import dataclass, field
from datetime import datetime
from .eventos import EventoDominio
import uuid
from pydispatch import dispatcher
import json
import pulsar
from pulsar.schema import *

cliente = pulsar.Client(f'pulsar://192.168.0.3:6650')
publicador = cliente.create_producer('eventos-orden')


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
        print("mas adentro....", evento)
        self.publicar_mensaje(evento)
        # dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)

    def limpiar_eventos(self):
        self.eventos = list()

    def publicar_mensaje(self, mensaje):
        # user_encode_data = pickle.dumps(mensaje)  # json.dumps(mensaje).encode('utf-8')
        user_encode_data = bytes(str(mensaje), 'utf-8')
        print("enviando evento a entrega", user_encode_data)
        publicador.send(user_encode_data)
        # cliente.close()
