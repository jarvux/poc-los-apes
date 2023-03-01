from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import re

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "a032d27b318022b08023e64b28a76a3bc060319760c6a918a4d6e9f643442364"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:GrupoC10@grupocloud.cer5khnfvz1u.us-east-1.rds.amazonaws.com:5432/proyecto"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'admin'

jwt = JWTManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @app.route("/api/auth/signup", methods=["POST"])
    def register():
        try:
            username = request.json.get("username", None)
            password = request.json.get("password", None)
            password2 = request.json.get("password2", None)
            email = request.json.get("email", None)

            if password != password2:
                return jsonify(error='Error: las contraseña de verificacion no coincide'), 400

            if re.fullmatch(r'[A-Za-z0-9@#$%&+=]{8,}', password):
                usuario = Usuario.query.filter(Usuario.username == username).first()
                if usuario is None:
                    entry = Usuario(username, email, password)
                    db.session.add(entry)
                    db.session.commit()
                    return jsonify(error='El usuario se creó correctamente'), 201
                else:
                    return jsonify(error='El usuario ya existe'), 400
            else:
                return jsonify(error='Error: la contraseña no cumple con las politicas minimas de seguridad.'), 400

        except:
            return jsonify(error='El usuario no se pudo registrar'), 400

    @app.route("/api/auth/login", methods=["POST"])
    def login():
        try:
            username = request.json.get("username", None)
            password = request.json.get("password", None)
            usuario = Usuario.query.filter(Usuario.username == username, Usuario.password == password).first()
            if usuario is None:
                return jsonify(error='Usuario y/o contraseña incorrecta'), 401
            else:
                access_token = create_access_token(identity=usuario.email)
                return jsonify(access_token=access_token), 200
        except:
            return jsonify(error='Error desconocido'), 500

    @app.route("/api/tokenInfo", methods=["GET"])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(email=current_user), 200


db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')