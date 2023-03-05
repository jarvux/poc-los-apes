import logging
import entregadelosalpes.seedwork.presentacion.api as api
import json
from entregadelosalpes.modulos.orden.aplicacion.servicios import ServicioOrden
from entregadelosalpes.modulos.orden.aplicacion.dto import OrdenDTO

from flask import redirect, render_template, request, session, url_for
from flask import Response
from entregadelosalpes.modulos.orden.aplicacion.mapeadores import MapeadorOrdenDTOJson

bp = api.crear_blueprint('ordenes', '/')

@bp.route('/ordenes', methods=('POST',))
def crear():
    try:
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        #print("orden_dto {orden_dict}", orden_dict)
        orden_dto = map_orden.externo_a_dto(orden_dict)
        print("orden_dto {orden_dto}", orden_dto)
        sr = ServicioOrden()
        dto_final = sr.crear_orden(orden_dto)
        print("dto_final {dto_final}", dto_final)
        return map_orden.dto_a_externo(dto_final)
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/ordenes', methods=('GET',))
@bp.route('/ordenes/<id>', methods=('GET',))
def dar_orden(id=None):
    if id:
        map_orden = MapeadorOrdenDTOJson()
        sr = ServicioOrden().obtener_orden_por_id(id)
        if sr : 
            return map_orden.dto_a_externo(sr)
        return [{'message': 'NOT FOUND'}]
    else:
        return [{'message': 'GET!'}]