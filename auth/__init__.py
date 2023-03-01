from flask import Flask

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='a032d27b318022b08023e64b28a76a3bc060319760c6a918a4d6e9f643442364'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app