
from __future__ import annotations
from dataclasses import dataclass, field
from entregadelosalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class OrdenCreada(EventoDominio):
    id_orden: uuid.UUID = None
    id_cliente: uuid.UUID = None
    items: str = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class OrdenDespachada(EventoDominio):
    id_orden: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class OrdenEntregada(EventoDominio):
    id_orden: uuid.UUID = None
    fecha_actualizacion: datetime = None
