from __future__ import annotations

from dataclasses import dataclass, field
from entregadelosalpes.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Orden, Producto
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class CodigoOrden(Codigo):
    ...

class EstadoOrden(str, Enum):
    CREADA = "Creada"
    DESPACHADA = "Despachada"
    ENTREGADA = "Entregada"

@dataclass(frozen=True)
class Orden(Orden):
    fecha_despacho: datetime
    fecha_entrega: datetime
    estado: EstadoOrden

    def fecha_despacho(self) -> datetime:
        return self.fecha_despacho

    def fecha_entrega(self) -> datetime:
        return self.fecha_entrega

    def estado(self) -> EstadoOrden:
        return self.estado

@dataclass(frozen=True)
class Items(ObjetoValor):
    productos: list[Producto] = field(default_factory=list)
