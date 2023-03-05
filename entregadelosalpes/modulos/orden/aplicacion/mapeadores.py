import logging
from entregadelosalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregadelosalpes.modulos.orden.dominio.entidades import Orden as OrdenEntidad
from entregadelosalpes.seedwork.dominio.objetos_valor import Producto
from entregadelosalpes.modulos.orden.dominio.objetos_valor import Orden
from .dto import OrdenDTO, ProductoDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_items(self, item: dict) -> ProductoDTO:
        print("MapeadorOrdenDTOJson _procesar_items aplicacion")
        producto_dto: ProductoDTO = ProductoDTO(item.get("fecha_creacion"), item.get("fecha_modificacion"), item.get("nombre"), item.get("precio"))
        return producto_dto

    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        print("MapeadorOrdenDTOJson externo_a_dto aplicacion")
        orden_dto = OrdenDTO()
        for itin in externo.get('items', list()):
            orden_dto.items.append(self._procesar_items(itin))

        print("MapeadorOrdenDTOJson externo_a_dto {orden}", orden_dto)
        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items(self, item_dto: ProductoDTO) -> Producto:
        print("MapeadorOrden _procesar_items aplicacion")
        fecha_creacion = datetime.strptime(item_dto.fecha_creacion, self._FORMATO_FECHA)
        fecha_modificacion = datetime.strptime(item_dto.fecha_modificacion, self._FORMATO_FECHA)
        nombre = item_dto.nombre
        precio = item_dto.precio
        producto: Producto = Producto(fecha_creacion, fecha_modificacion, nombre, precio)

        return producto

    def obtener_tipo(self) -> type:
        return OrdenEntidad.__class__

    def entidad_a_dto(self, entidad: OrdenEntidad) -> OrdenDTO:
        print("MapeadorOrden entidad_a_dto aplicacion")
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        items = list()
        print("--****items***--",entidad.items)
        for itin in entidad.items:
            print("--****itin***--",itin)
            fecha_creacion = itin.fecha_creacion
            fecha_modificacion = itin.fecha_modificacion
            nombre = itin.nombre
            precio = itin.precio
            producto = ProductoDTO(fecha_creacion=fecha_creacion,fecha_modificacion=fecha_modificacion, nombre=nombre, precio=precio)
            items.append(producto)
        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id, items)

    def dto_a_entidad(self, dto: OrdenDTO) -> OrdenEntidad:
        print("MapeadorOrden dto_a_entidad aplicacion")
        print("MapeadorOrden Orden entidad {orden}", OrdenEntidad())
        orden = OrdenEntidad()
        items_dto: list[ProductoDTO] = list()
        orden.items = list()
        if dto : 
           items_dto = dto.items

        for itin in items_dto:
            print("MapeadorOrden dto_a_entidad aplicacion item {itin}", itin)
            orden.items.append(self._procesar_items(itin))
        
        return orden
