from authentication.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint


Base = db.declarative_base()


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        db.UniqueConstraint('name', name='unique_component_commit'),
    )
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
