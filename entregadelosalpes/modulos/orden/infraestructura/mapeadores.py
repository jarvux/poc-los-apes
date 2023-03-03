from entregadelosalpes.seedwork.dominio.repositorios import Mapeador
from entregadelosalpes.modulos.orden.dominio.objetos_valor import Orden, Items
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Items, Producto
from .dto import Orden as OrdenDTO
from .dto import Items as ItemsDTO

class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items_dto(self, items_dto: list) -> list[Items]:
        for itin in items_dto:
            productos = list()
            for productos_dict in itin.productos():
                nombre = productos_dict.nombre.get("nombre")
                precio = productos_dict.precio.get("precio")
                fecha_creacion = productos_dict.fecha_creacion.get("fecha_creacion")
                fecha_modificacion = productos_dict.fecha_modificacion.get("fecha_modificacion")
                productos.append(Producto(nombre, precio, fecha_creacion, fecha_modificacion))

        return [Items(productos)]

    def _procesar_items(self, items: any) -> list[ItemsDTO]:
        items_dto = list()

        for i, producto in enumerate(items.productos):
            item_dto = ItemsDTO()
            item_dto.nombre = producto.nombre
            item_dto.precio = producto.precio
            item_dto.fecha_creacion = producto.fecha_creacion
            item_dto.fecha_modificacion = producto.fecha_modificacion
            item_dto.producto_orden = i
            items_dto.append(item_dto)
        return items_dto

    def obtener_tipo(self) -> type:
        return Reserva.__class__

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
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
        orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        orden.items = list()

        items_dto: list[ItemsDTO] = dto.items

        orden.items.extend(self._procesar_items_dto(items_dto))
        
        return orden