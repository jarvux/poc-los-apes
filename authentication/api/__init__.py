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

     # Inicializa la DB
    from authentication.config.db import init_db
    init_db(app)

    from authentication.config.db import db

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
