from auth import create_app
from flask_restful import Api
from .models import db
from .views import \
    ViewSignIn, \
    ViewSignIn

from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(ViewSignIn, '/signIn')
api.add_resource(ViewSignIn, '/logIn')
jwt = JWTManager(app)