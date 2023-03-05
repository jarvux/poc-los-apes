from dataclasses import dataclass, field
from datetime import datetime
from entregadelosalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProductoDTO(DTO):
    fecha_creacion: str
    fecha_modificacion: str
    nombre: str
    precio: str

@dataclass(frozen=True)
class ItemsDTO(DTO):
    productos: list[ProductoDTO]

@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: datetime = field(default_factory=str)
    fecha_actualizacion: datetime = field(default_factory=str)
    id: str = field(default_factory=str)
    items: list[ProductoDTO] = field(default_factory=list)