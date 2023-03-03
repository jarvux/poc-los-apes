from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):
    codigo: str

class Orden(ABC, ObjetoValor):
    @abstractmethod
    def fecha_creacion(self) -> datetime:
        ...
    
    @abstractmethod
    def fecha_actualizacion(self) -> datetime:
        ...

@dataclass(frozen=True)
class Producto(ObjetoValor):
    nombre: str
    precio: str
    fecha_creacion: str
    fecha_modificacion: str

