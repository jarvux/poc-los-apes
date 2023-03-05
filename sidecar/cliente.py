from __future__ import print_function

from google.protobuf.timestamp_pb2 import Timestamp
from entregadelosalpes.pb2py import orden_pb2
from entregadelosalpes.pb2py import orden_pb2_grpc

import logging
import grpc
import datetime
import os
import json


def importar_comando_orden(json_file):
    json_dict = json.load(json_file)

    # Transformamos en 
    items = json_dict['items']

    TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    for item in items:
        item['fecha_creacion'] = datetime.datetime.strptime(item['fecha_creacion'], TIMESTAMP_FORMAT)
        item['fecha_modificacion'] = datetime.datetime.now()

    return json_dict

def dict_a_proto_orden(dict_orden):
    items = list()
    for itin in dict_orden.get('items', []):
        nombre = itin['nombre']
        precio = itin['precio']

        fecha_creacion = Timestamp()
        fecha_creacion.FromSeconds(int(itin['fecha_creacion'].timestamp()))

        fecha_modificacion = Timestamp()
        fecha_modificacion.FromSeconds(int(itin['fecha_modificacion'].timestamp()))
        items.append(orden_pb2.Producto(fecha_creacion=fecha_creacion, fecha_modificacion=fecha_modificacion, nombre=nombre, precio=precio))

    return orden_pb2.Orden(id=dict_orden.get('id'), items=items)

def run():
    print("Crear una orden")
    with grpc.insecure_channel('localhost:50051') as channel:
        pathFile  = os.path.dirname(__file__)
        print('File pathFile {pathFile}', pathFile)
        json_file = open(f"{os.path.dirname(__file__)}/mensajes/crear_orden.json")

        json_dict = importar_comando_orden(json_file)
        orden = dict_a_proto_orden(json_dict)

        stub = orden_pb2_grpc.OrdenesStub(channel)
        response = stub.CrearOrden(orden)
    print("Greeter client received: " + response.mensaje)
    print(f'Orden: {response.orden}')


if __name__ == '__main__':
    logging.basicConfig()
    run()