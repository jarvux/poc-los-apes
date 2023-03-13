import pulsar,_pulsar  
from pulsar.schema import *

from entrega.modulos.entrega.infraestructura.schema.v1.eventos import EventoOrdenCreada
from entrega.seedwork.infraestructura import utils

cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
print("cliente", cliente)
consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregadelosalpes-sub-eventos', _schema_definition=AvroSchema(EventoOrdenCreada))

while True:
    mensaje = consumidor.receive()
    datos = mensaje.value().data
    print(f'Evento recibido: {datos}')
    consumidor.acknowledge(mensaje)   
