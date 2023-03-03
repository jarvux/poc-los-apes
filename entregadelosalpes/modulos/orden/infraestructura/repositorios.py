from entregadelosalpes.config.db import db
from entregadelosalpes.modulos.orden.dominio.repositorios import RepositorioOrdenes, RepositorioProductos
from entregadelosalpes.modulos.orden.dominio.objetos_valor import Orden, Producto
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Items, Producto
from entregadelosalpes.modulos.orden.dominio.fabricas import FabricaOrdenes
from .dto import Orden as OrdenDTO
from .mapeadores import MapeadorOrden
from uuid import UUID

class RepositorioProductosSQLite(RepositorioProductos):

    def obtener_por_id(self, id: UUID) -> Producto:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Producto]:
        nombre="Cape Town International"
        precio="150"
        fecha_creacion="12-02-2023"
        fecha_modificacion ="12-02-2023"
        producto = Producto(nombre, precio, fecha_creacion, fecha_modificacion)
        return [producto]

    def agregar(self, entity: Producto):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Producto):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioOrdenesSQLite(RepositorioOrdenes):

    def __init__(self):
        self._fabrica_ordenes: FabricaOrdenes = FabricaOrdenes()

    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes

    def obtener_por_id(self, id: UUID) -> Orden:
        orden_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        return self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())

    def obtener_todos(self) -> list[Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        orden_dto = self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())
        db.session.add(orden_dto)
        db.session.commit()

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError