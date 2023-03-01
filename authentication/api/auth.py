import json
from flask import Response, request, jsonify
from authentication.modules.auth.application.mappers import MapperAuthDTOJson, MapperLoginDTOJson
from authentication.seedwork.domain.exceptions import ExceptionDomain
from authentication.modules.auth.application.services import ServiceUser, ServiceToken
import authentication.seedwork.presentation.api as api

bp = api.crear_blueprint('users', '/users')


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


@bp.route('/logIn', methods=('POST',))
def logIn():
    try:
        user_dict = request.json
        map_login = MapperLoginDTOJson()
        user_dto = map_login.ext_to_dto(user_dict)

        sr = ServiceUser()
        user = sr.get_user(user_dto)

        token_sr = ServiceToken()
        token = token_sr.create_token(user)
        return jsonify(access_token=token), 200
    except ExceptionDomain as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
