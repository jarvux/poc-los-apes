import os
from flask import Flask

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def importar_modelos_alchemy():
    pass


def registrar_handlers():
    pass


def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la DB
    from entregadelosalpes.config.db import init_db
    init_db(app)

    from entregadelosalpes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()

    # Importa Blueprints
    from .orden import bp

    # Registro de Blueprints
    app.register_blueprint(orden.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app