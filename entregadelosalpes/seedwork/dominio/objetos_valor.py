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
    def fecha_creacion(self) -> str:
        ...
    
    @abstractmethod
    def fecha_actualizacion(self) -> str:
        ...

@dataclass(frozen=True)
class Producto(ObjetoValor):
    fecha_creacion: str
    fecha_actualizacion: str
    nombre: str
    precio: str

