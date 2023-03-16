import json
import pickle

import pulsar, _pulsar
from pulsar.schema import *


def serve():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://192.168.0.3:6650')
        print("cliente", cliente)
        consumidor = cliente.subscribe('eventos-orden', 'eventos-orden')

        while True:
            mensaje = consumidor.receive()
            print(type(mensaje.value()))
            output = str(mensaje.value())
            print(f'Orden entregada cliente: {output}')
            consumidor.acknowledge(mensaje)
        cliente.close()
    except Exception as e:
        print('ERROR: serve!', e)


if __name__ == '__main__':
    serve()
