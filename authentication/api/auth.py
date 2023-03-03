import json
from flask import Response, request
from authentication.modules.auth.application.mappers import MapperAuthDTOJson
from authentication.seedwork.domain.exceptions import ExceptionDomain
from authentication.modules.auth.application.services import ServiceUser
from authentication.seedwork.presentation.api import api

bp = api.crear_blueprint('signIn', '/signIn')

@bp.route('/signIn', methods=('POST',))
def signIn():
    try:
        user_dict = request.json

        map_reserva = MapperAuthDTOJson()
        user_dto = map_reserva.ext_to_dto(user_dict)
        
        sr = ServiceUser()
        dto_final = sr.create_user(user_dto)
        
        return map_reserva.dto_to_ext(dto_final)
    except ExceptionDomain as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')