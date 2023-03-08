from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from entregadelosalpes.seedwork.dominio.objetos_valor import Producto
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.eventos import OrdenCreada, OrdenDespachada, OrdenEntregada
from entregadelosalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Producto(Entidad):
    nombre: str = field(hash=True, default=None)
    precio: str = field(hash=True, default=None)

@dataclass
class Orden(AgregacionRaiz):
    id_orden: uuid.UUID = field(hash=True, default=None)
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.CREADA)
    items: list[Producto] = field(default_factory=list[Producto])

    def crear_orden(self, orden: Orden):
        self.items = orden.items
        self.agregar_evento(OrdenCreada(id_orden=self.id, id_cliente=self.id_cliente, estado=self.estado, fecha_creacion=self.fecha_creacion))
        
    def despachar_orden(self):
        self.estado = ov.EstadoOrden.DESPACHADA
        #self.agregar_evento(OrdenDespachada(self.id, self.fecha_actualizacion))

    def entregar_orden(self):
        self.estado = ov.EstadoOrden.ENTREGADA
        #self.agregar_evento(OrdenEntregada(self.id, self.fecha_actualizacion))
