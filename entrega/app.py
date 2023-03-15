import json

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
            datos = json.loads(mensaje.value())
            print(f'Orden entregada cliente: {datos}')
            consumidor.acknowledge(mensaje)
        cliente.close()
    except:
        logging.error('ERROR: serve!')
        traceback.print_exc()


if __name__ == '__main__':
    serve()
