import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from entregadelosalpes.modulos.orden.infraestructura.schema.v1.eventos import EventoOrdenCreada
from entregadelosalpes.modulos.orden.infraestructura.schema.v1.comandos import ComandoCrearOrden
from entregadelosalpes.seedwork.infraestructura import utils


cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
print("cliente",cliente)
consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregadelosalpes-sub-eventos', _schema_definition=AvroSchema(EventoOrdenCreada))

while True:
    mensaje = consumidor.receive()
    datos = mensaje.value().data
    print(f'Evento recibido: {datos}')
    consumidor.acknowledge(mensaje)   
