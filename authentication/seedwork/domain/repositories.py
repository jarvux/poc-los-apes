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
    def add(self, entity: Entidad):
        ...

    @abstractmethod
    def actualizar(self, entity: Entidad):
        ...

    @abstractmethod
    def eliminar(self, entity_id: UUID):
        ...

    @abstractmethod
    def get_user(self, name: str, password) -> Entidad:
        ...


class Mapper(ABC):
    @abstractmethod
    def get_type(self) -> type:
        ...

    @abstractmethod
    def entity_to_dto(self, entidad: Entidad) -> any:
        ...

    @abstractmethod
    def dto_to_entity(self, dto: any) -> Entidad:
        ...
