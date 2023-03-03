from entregadelosalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
ordenes_items = db.Table(
    "ordenes_items",
    db.Model.metadata,
    db.Column("orden_id", db.String, db.ForeignKey("ordenes.id")),
    db.Column("producto_orden", db.Integer),
    db.Column("fecha_creacion", db.DateTime),
    db.Column("fecha_modificacion", db.DateTime),
    db.Column("nombre", db.String),
    db.Column("precio", db.String),
    db.ForeignKeyConstraint(
        ["producto_orden", "fecha_creacion", "fecha_modificacion", "nombre", "precio"],
        ["items.producto_orden", "items.fecha_creacion", "items.fecha_modificacion", "items.nombre", "items.precio"]
    )
)

class Items(db.Model):
    __tablename__ = "items"
    producto_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, primary_key=True)
    fecha_modificacion= db.Column(db.DateTime, nullable=False, primary_key=True)
    nombre = db.Column(db.String, nullable=False, primary_key=True)
    precio= db.Column(db.String, nullable=False, primary_key=True)


class Orden(db.Model):
    __tablename__ = "ordenes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    items = db.relationship('Items', secondary=ordenes_items, backref='ordenes')