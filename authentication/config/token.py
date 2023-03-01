from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import Flask

jwt = None


def init_token_manager(app: Flask):
    global jwt
    jwt = JWTManager(app)
