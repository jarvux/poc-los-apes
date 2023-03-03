from abc import ABC
from entregadelosalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioOrdenes(Repositorio, ABC):
    ...

class RepositorioProductos(Repositorio, ABC):
    ...