import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
import aiopulsar
import json
from entregadelosalpes.modulos.orden.infraestructura.schema.v1.eventos import EventoOrdenCreada
from entregadelosalpes.modulos.orden.infraestructura.schema.v1.comandos import ComandoCrearOrden
from entregadelosalpes.seedwork.infraestructura import utils

from entregadelosalpes.modulos.orden.aplicacion.mapeadores import MapeadorOrdenDTOJson
from entregadelosalpes.modulos.orden.aplicacion.servicios import ServicioOrden

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client('pulsar://192.168.0.3:6650')
        
        consumidor = cliente.subscribe('nueva-orden','nueva-orden')
        while True:
            mensaje = consumidor.receive()
            print("llego mensaje",mensaje)
            datos = json.loads(mensaje.value())
            
            crear_orden_evento(datos)
            print(f'Evento recibido: {datos}')
            consumidor.acknowledge(mensaje) 
        cliente.close()
        


    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()


def crear_orden_evento(orden_dict):
    map_orden = MapeadorOrdenDTOJson()
    #print("orden_dto {orden_dict}", orden_dict)
    orden_dto = map_orden.externo_a_dto(orden_dict)
    #print("orden_dto {orden_dto}", orden_dto)
    sr = ServicioOrden()
    dto_final = sr.crear_orden(orden_dto)
    #print("dto_final {dto_final}", dto_final)
    return map_orden.dto_a_externo(dto_final)