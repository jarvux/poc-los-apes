import logging
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Producto
from .dto import Orden as OrdenDTO
from .dto import Producto as ProductoDTO
import uuid
class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items_dto(self, items_dto: list) -> list[Producto]:
        print("MapeadorOrden _procesar_items_dto infra")
        productos = list()
        print("XXXXXXXitems_dto",items_dto)
        for itin in items_dto:
            print("MapeadorOrden _procesar_items_dto infra producto {itin}", itin)
            fecha_creacion = itin.fecha_creacion
            fecha_modificacion = itin.fecha_modificacion
            nombre = itin.nombre
            precio = itin.precio
            productos.append(Producto(fecha_creacion, fecha_modificacion, nombre, precio))

        return [productos]

    def _procesar_items(self, items: any) -> list[ProductoDTO]:
        items_dto = list()
        print("MapeadorOrden _procesar_items infra",items)
        for producto in items:
            print("MapeadorOrden _procesar_items infra producto {producto}", producto.fecha_creacion)
            item_dto = ProductoDTO()
            item_dto.fecha_creacion = producto.fecha_creacion
            item_dto.fecha_modificacion = producto.fecha_modificacion
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
        orden_dto.fecha_creacion = entidad.fecha_creacion
        orden_dto.fecha_actualizacion = entidad.fecha_actualizacion
        orden_dto.id = str(entidad.id)
        orden_dto.items = self._procesar_items(entidad.items)

        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        print("MapeadorOrden dto_a_entidad infra")
        orden = None
        if dto : 
            orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
            orden.items = list()
            if dto : 
              items_dto: list[ProductoDTO] = dto.items
            print("MapeadorOrden dto_a_entidad infra items_dto {items_dto}", items_dto)
            orden.items = self._procesar_items_dto(items_dto)
        return orden