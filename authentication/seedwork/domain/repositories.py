
from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Entidad

class Repository(ABC):
    @abstractmethod
    def obtener_por_id(self, id: UUID) -> Entidad:
        ...

    @abstractmethod
    def obtener_todos(self) -> list[Entidad]:
        ...

    @abstractmethod
    def agregar(self, entity: Entidad):
        ...

    @abstractmethod
    def actualizar(self, entity: Entidad):
        ...

    @abstractmethod
    def eliminar(self, entity_id: UUID):
        ...
        
class Mapper(ABC):
    @abstractmethod
    def obtener_tipo(self) -> type:
        ...

    @abstractmethod
    def entidad_a_dto(self, entidad: Entidad) -> any:
        ...

    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entidad:
        ...
    