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

    # Importa Blueprints
    from .orden import bp

    # Registro de Blueprints
    app.register_blueprint(orden.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app