import logging
import entregadelosalpes.seedwork.presentacion.api as api
import json
import pulsar
from pulsar.schema import *

from flask import redirect, render_template, request, session, url_for

bp = api.crear_blueprint('ordenes', '/')

client = pulsar.Client('pulsar://192.168.0.3:6650')
producer = client.create_producer('nueva-orden')

@bp.route('/ordenes', methods=('POST',))
def crear():
    try:
        orden_dict = request.json
        user_encode_data = json.dumps(orden_dict).encode('utf-8')
        print(user_encode_data)

        producer.send(user_encode_data)
        return "Evento Enviado", 200
    except Exception as e:
        return str(e), 400
