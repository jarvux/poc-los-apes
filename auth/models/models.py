from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

role_assigned_user = db.Table('role_assigned_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key = True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    roles = db.relationship('Role', secondary='role_assigned_user', back_populates="users")

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User', secondary='role_assigned_user', back_populates="roles")

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = User
         include_relationships = True
         load_instance = True

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Role
         include_relationships = True
         load_instance = True
