import logging
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Producto
from .dto import Orden as OrdenDTO
from .dto import Producto as ProductoDTO

class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items_dto(self, items_dto: list) -> list[Producto]:
        print("MapeadorOrden _procesar_items_dto infra")
        productos = list()
        for itin in items_dto:
            print("MapeadorOrden _procesar_items_dto infra producto {itin}", itin)
            fecha_creacion = itin.fecha_creacion.get("fecha_creacion")
            fecha_modificacion = itin.fecha_modificacion.get("fecha_modificacion")
            nombre = itin.get("nombre")
            precio = itin.get("precio")
            productos.append(Producto(fecha_creacion, fecha_modificacion, nombre, precio))

        return [productos]

    def _procesar_items(self, items: any) -> list[ProductoDTO]:
        items_dto = list()
        print("MapeadorOrden _procesar_items infra")
        for i, producto in enumerate(items):
            print("MapeadorOrden _procesar_items infra producto {producto}", producto)
            item_dto = ProductoDTO()
            item_dto.fecha_creacion = producto.fecha_creacion
            item_dto.fecha_modificacion = producto.fecha_modificacion
            item_dto.nombre = producto.nombre
            item_dto.precio = producto.precio
            item_dto.producto_orden = i
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

        items_dto = list()
        for item in entidad.items:
            items_dto.extend(self._procesar_items(item))

        orden_dto.items = items_dto

        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        print("MapeadorOrden dto_a_entidad infra")
        orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        orden.items = list()
        items_dto: list[ProductoDTO] = dto.items
        print("MapeadorOrden dto_a_entidad infra items_dto {items_dto}", items_dto)
        orden.items.extend(self._procesar_items_dto(items_dto))

        return orden