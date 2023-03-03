import entregadelosalpes.seedwork.presentacion.api as api
import json
from entregadelosalpes.modulos.orden.aplicacion.servicios import ServicioOrden
from entregadelosalpes.modulos.orden.aplicacion.dto import OrdenDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from entregadelosalpes.modulos.orden.aplicacion.mapeadores import MapeadorOrdenDTOJson

bp = api.crear_blueprint('ordenes', '/ordenes')

@bp.route('/ordenes', methods=('POST',))
def crear():
    try:
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)

        sr = ServicioOrden()
        dto_final = sr.crear_orden(orden_dto)

        return map_orden.dto_a_externo(dto_final)
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/ordenes', methods=('GET',))
@bp.route('/ordenes/<id>', methods=('GET',))
def dar_orden(id=None):
    if id:
        sr = ServicioOrden()
        
        return sr.obtener_orden_por_id(id)
    else:
        return [{'message': 'GET!'}]