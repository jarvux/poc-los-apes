import os
from flask import Flask

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


    
def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    return app