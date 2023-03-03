from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from entregadelosalpes.seedwork.dominio.objetos_valor import Producto
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.eventos import OrdenCreada, OrdenDespachada, OrdenEntregada
from entregadelosalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Items(Entidad):
    productos: list[ov.Items] = field(default_factory=list[ov.Items])

    def obtener_items(self, productos: list[Producto]):
        return self.productos

@dataclass
class Orden(AgregacionRaiz):
    id_orden: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.CREADA)
    items: list[ov.Items] = field(default_factory=list[ov.Items])

    def crear_orden(self, orden: Orden):
        self.id_orden = orden.id_orden
        self.estado = orden.estado
        self.items = orden.items
        self.agregar_evento(OrdenCreada(id_orden=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def despachar_orden(self):
        self.estado = ov.EstadoOrden.DESPACHADA
        self.agregar_evento(OrdenDespachada(self.id, self.fecha_actualizacion))

    def entregar_orden(self):
        self.estado = ov.EstadoOrden.ENTREGADA
        self.agregar_evento(OrdenEntregada(self.id, self.fecha_actualizacion))
