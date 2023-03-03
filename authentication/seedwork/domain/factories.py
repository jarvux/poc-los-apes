from abc import ABC, abstractmethod
from .repositories import Mapper
from .mixins import ValidarReglasMixin

class Fabrica(ABC, ValidarReglasMixin):
    @abstractmethod
    def crear_objeto(self, obj: any, mapeador: Mapper=None) -> any:
        ...