from entregadelosalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregadelosalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregadelosalpes.modulos.orden.dominio.entidades import Orden
from entregadelosalpes.seedwork.dominio.objetos_valor import Producto
from entregadelosalpes.modulos.orden.dominio.objetos_valor import Orden, Items
from .dto import OrdenDTO, ItemsDTO, ProductoDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_items(self, items: dict) -> ItemsDTO:
        productos_dto: list[ProductoDTO] = list()
        for item in items.get('productos', list()):
            producto_dto: ProductoDTO = ProductoDTO(item.get('fecha_creacion'), item.get('fecha_modificacion'), item.get('nombre'), item.get('precio')) 
            productos_dto.append(Producto(producto_dto))

        return ItemsDTO(productos_dto)

    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        items: list[ItemsDTO] = list()
        for itin in externo.get('items', list()):
            orden_dto.items.append(self._procesar_items(itin))

        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items(self, item_dto: ItemsDTO) -> Items:
        productos = list()

        for producto_dto in item_dto.productos:
            nombre = producto_dto.nombre.get('nombre')
            precio = producto_dto.precio.get('precio')
            fecha_creacion = datetime.strptime(producto_dto.fecha_creacion, self._FORMATO_FECHA)
            fecha_modificacion = datetime.strptime(producto_dto.fecha_modificacion, self._FORMATO_FECHA)

            producto: Producto = Producto(fecha_creacion, fecha_modificacion, nombre, precio)
            
            productos.append(producto)

        return Items(productos)

    def obtener_tipo(self) -> type:
        return Orden.__class__

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        items = list()

        for itin in entidad.items:
            productos = list()
            for item in itin.productos:
                fecha_creacion = item.fecha_creacion.strftime(self._FORMATO_FECHA)
                fecha_modificacion = item.fecha_modificacion.strftime(self._FORMATO_FECHA)
                nombre = item.nombre
                precio = item.precio
                producto = ProductoDTO(fecha_creacion=fecha_creacion, fecha_modificacion=fecha_modificacion, nombre=nombre, precio=precio)
                
                productos.append(producto)
            items.append(ItemsDTO(productos))
        
        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id, items)

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.items = list()

        items_dto: list[ItemsDTO] = dto.items

        for itin in items_dto:
            orden.items.append(self._procesar_items(itin))
        
        return orden

