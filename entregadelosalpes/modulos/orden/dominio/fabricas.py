from .entidades import Orden
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador
from entregadelosalpes.seedwork.dominio.fabricas import Fabrica
from entregadelosalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden = mapeador.dto_a_entidad(obj)
            return orden

@dataclass
class FabricaOrdenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrden()
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise Exception("Mensaje Error Fabrica")