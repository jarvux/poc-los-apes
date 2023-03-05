from concurrent import futures
import logging

import grpc
from entregadelosalpes.pb2py import orden_pb2
from entregadelosalpes.pb2py import orden_pb2_grpc


from entregadelosalpes.servicios.orden import Orden

def agregar_servicios(servidor):
    orden_pb2_grpc.add_OrdenesServicer_to_server(Orden(), servidor)

def serve():
    port = '50051'
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agregar_servicios(servidor)

    servidor.add_insecure_port('[::]:' + port)
    servidor.start()
    print("Servidor corriendo por el puerto:" + port)
    servidor.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()