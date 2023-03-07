import json
import requests
import datetime
import os

from entregadelosalpes.pb2py.orden_pb2 import Orden, RespuestaOrden
from entregadelosalpes.pb2py.orden_pb2_grpc import OrdenesServicer

from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Ordenes(OrdenesServicer):
    HOSTNAME_ENV: str = 'ENTREGADELOSALPES_ADDRESS'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5000'
    REST_API_ENDPOINT: str = '/ordenes'

    def CrearOrden(self, request, context):
        dict_obj = MessageToDict(request, preserving_proto_field_name=True)

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 200:
            respuesta = json.loads(r.text)

            fecha_creacion = respuesta['fecha_creacion']
            fecha_actualizacion = respuesta['fecha_actualizacion']

            orden = Orden(fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, items=respuesta.get('items',[]))

            return RespuestaOrden(mensaje='OK', orden=orden)
        else:
            return RespuestaOrden(mensaje=f'Error: {r.status_code}')

    def ConsultarOrden(self, request, context):
        # TODO
        raise NotImplementedError