import logging
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Producto
from .dto import Orden as OrdenDTO
from .dto import Producto as ProductoDTO
import uuid

from entregadelosalpes.modulos.orden.dominio.eventos import OrdenCreada
class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items_dto(self, items_dto: list) -> list[ov.Producto]:
        productos = list()
        item_dict = dict()
        for itin in items_dto:
            print("MapeadorOrden _procesar_items_dto infra producto {itin}", itin)
            fecha_creacion = itin.fecha_creacion
            fecha_actualizacion = itin.fecha_actualizacion
            nombre = itin.nombre
            precio = itin.precio
            item_dict.setdefault(str(itin.producto_orden), Producto(fecha_creacion, fecha_actualizacion, nombre, precio))

        for k, producto in item_dict.items():
            productos.append(producto)

        return productos

    def _procesar_items(self, items: any) -> list[ProductoDTO]:
        items_dto = list()
        print("MapeadorOrden _procesar_items infra",items)
        for k, producto in enumerate(items):
            item_dto = ProductoDTO()
            item_dto.fecha_creacion = producto.fecha_creacion
            item_dto.fecha_actualizacion = producto.fecha_actualizacion
            item_dto.nombre = producto.nombre
            item_dto.precio = producto.precio
            item_dto.producto_orden = str(uuid.uuid4())
            items_dto.append(item_dto)
        return items_dto

    def obtener_tipo(self) -> type:
        return Orden.__class__

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        print("MapeadorOrden entidad_a_dto infra")
        orden_dto = OrdenDTO()
        orden_dto.fecha_creacion = str(entidad.fecha_creacion)
        orden_dto.fecha_actualizacion = str(entidad.fecha_actualizacion)
        orden_dto.id = str(entidad.id)
        orden_dto.items = self._procesar_items(entidad.items)

        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.items = list()
        items_dto: list[ProductoDTO] = dto.items

        print("MapeadorOrden dto_a_entidad infra items_dto {items_dto}", items_dto)
        orden.items.extend(self._procesar_items_dto(items_dto))

        return orden
            
class MapadeadorEventosOrden(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            OrdenCreada: self._entidad_a_reserva_creada,
        }

    def obtener_tipo(self) -> type:
        return OrdenCreada.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_orden_creada(self, entidad: OrdenCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import OrdenCreadaPayload, EventoOrdenCreada
            payload = OrdenCreadaPayload(
                id_orden=str(evento.id_orden), 
                id_cliente=str(evento.id_cliente), 
                items=str(evento.items), 
                fecha_creacion= str(evento.fecha_creacion)
            )
            evento_integracion = EventoOrdenCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'OrdenCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'entregadelosalpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)       