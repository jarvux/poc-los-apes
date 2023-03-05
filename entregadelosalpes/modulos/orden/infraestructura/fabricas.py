
from dataclasses import dataclass, field
from entregadelosalpes.seedwork.dominio.fabricas import Fabrica
from entregadelosalpes.seedwork.dominio.repositorios import Repositorio
from entregadelosalpes.modulos.orden.dominio.repositorios import RepositorioOrdenes, RepositorioProductos
from .repositorios import RepositorioOrdenesSQLite, RepositorioProductosSQLite

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes.__class__:
            return RepositorioOrdenesSQLite()
        elif obj == RepositorioProductos.__class__:
            return RepositorioProductosSQLite()
        else:
            raise Exception("Error Fabricas Ordenes")