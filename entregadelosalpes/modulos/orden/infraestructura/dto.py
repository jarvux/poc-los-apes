from entregadelosalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
orden_productos = db.Table(
    "orden_productos",
    db.Model.metadata,
    db.Column("orden_id", db.String, db.ForeignKey("orden.id")),
    db.Column("producto_orden", db.Integer),
    db.Column("fecha_creacion", db.String),
    db.Column("fecha_modificacion", db.String),
    db.Column("nombre", db.String),
    db.Column("precio", db.String),
    db.ForeignKeyConstraint(
        ["producto_orden", "fecha_creacion", "fecha_modificacion", "nombre", "precio"],
        ["producto.producto_orden", "producto.fecha_creacion", "producto.fecha_modificacion", "producto.nombre", "producto.precio"]
    )
)

class Producto(db.Model):
    __tablename__ = "producto"
    producto_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha_creacion = db.Column(db.String, nullable=False, primary_key=True)
    fecha_modificacion= db.Column(db.String, nullable=False, primary_key=True)
    nombre = db.Column(db.String, nullable=False, primary_key=True)
    precio = db.Column(db.String, nullable=False, primary_key=True)


class Orden(db.Model):
    __tablename__ = "orden"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    items = db.relationship('Producto', secondary=orden_productos, backref='orden')