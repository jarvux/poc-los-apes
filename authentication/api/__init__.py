import os
from flask import Flask

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def importar_modelos_alchemy():
    import authentication.modules.auth.infrastructure.dto
    
    
def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'users.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # jwt config
    app.config["JWT_SECRET_KEY"] = "a032d27b318022b08023e64b28a76a3bc060319760c6a918a4d6e9f643442364"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    app.secret_key = 'admin'

     # Inicializa la DB
    from authentication.config.db import init_db
    init_db(app)

    from authentication.config.db import db

    # init jwt
    from authentication.config.token import init_token_manager
    init_token_manager(app)

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()


     # Importa Blueprints
    from . import auth
     
     # Registro de Blueprints
    app.register_blueprint(auth.bp)
     
    
    @app.route("/ping")
    def health():
        return "pong"

    return app
