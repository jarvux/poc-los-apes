from flask import request
from ..models import db, User, Role
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sqlalchemy.exc import IntegrityError


class ViewSignIn(Resource):

    def post(self):
        try:
            userExist = User.query.filter(User.name == request.json["user"]).first()
            if userExist is None:
                nuevo_usuario = User(name=request.json["user"], password=request.json["password"])
                role = request.json["role"]
                rol = Role.query.get_or_404(role)
                rol.users.append(nuevo_usuario)
                db.session.commit()
                token_de_acceso = create_access_token(identity=nuevo_usuario.id)
                return {"message": "User created successfully", "token": token_de_acceso}
            else:
                return 'The user already exist with that role', 409
        except IntegrityError:
            db.session.rollback()
            return 'The user already exist with that role', 409

    def delete(self, id_user):
        user = User.query.get_or_404(id_user)
        db.session.delete(user)
        db.session.commit()
        return 'User deleted', 204


class ViewLogIn(Resource):

    def post(self):
        user = User.query.filter(User.name == request.json["user"],
                                 User.password == request.json["password"]).first()
        db.session.commit()
        if user is None:
            return "The user // password does not exist", 404
        else:
            token_de_acceso = create_access_token(identity=user.id)
            return {"message": "User created successfully", "token": token_de_acceso}
