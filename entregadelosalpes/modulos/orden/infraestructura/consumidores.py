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

from entregadelosalpes.modulos.orden.aplicacion.mapeadores import MapeadorOrdenDTOJson
from entregadelosalpes.modulos.orden.aplicacion.servicios import ServicioOrden

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('new-order')

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('nueva-orden', 'nueva-orden')

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje}')
            datos = mensaje.value()
            print(f'Evento recibido: {datos}')

            crear_orden_evento(datos)

            consumidor.acknowledge(mensaje)

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def crear_orden_evento(orden_dict):
    map_orden = MapeadorOrdenDTOJson()
    #print("orden_dto {orden_dict}", orden_dict)
    orden_dto = map_orden.externo_a_dto(orden_dict)
    #print("orden_dto {orden_dto}", orden_dto)
    sr = ServicioOrden()
    dto_final = sr.crear_orden(orden_dto)
    #print("dto_final {dto_final}", dto_final)
    return map_orden.dto_a_externo(dto_final)