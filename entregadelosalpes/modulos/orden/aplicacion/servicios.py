from urllib import response
from entregadelosalpes.seedwork.aplicacion.servicios import Servicio
from entregadelosalpes.modulos.orden.dominio.entidades import Orden
from entregadelosalpes.modulos.orden.dominio.fabricas import FabricaOrdenes
from entregadelosalpes.modulos.orden.infraestructura.fabricas import FabricaRepositorio
from entregadelosalpes.modulos.orden.infraestructura.repositorios import RepositorioOrdenes
#from entregadelosalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorOrden

from .dto import OrdenDTO

import asyncio

class ServicioOrden(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_orden: FabricaOrdenes = FabricaOrdenes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ordenes(self):
        return self._fabrica_orden       
    
    def crear_orden(self, orden_dto: OrdenDTO) -> OrdenDTO:
        orden: Orden = self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())
        #orden.crear_orden(orden)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        repositorio.agregar(orden) 
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()

        return self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())

    def obtener_orden_por_id(self, id) -> OrdenDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        #return self.fabrica_ordenes.crear_objeto(repositorio.obtener_por_id(id), MapeadorOrden())
        return repositorio.obtener_por_id(id)
