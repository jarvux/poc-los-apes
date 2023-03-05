from entregadelosalpes.config.db import db
from entregadelosalpes.modulos.orden.dominio.repositorios import RepositorioOrdenes, RepositorioProductos
import entregadelosalpes.modulos.orden.dominio.objetos_valor as ov
from entregadelosalpes.modulos.orden.dominio.entidades import Orden, Producto
from entregadelosalpes.modulos.orden.dominio.fabricas import FabricaOrdenes
from .dto import Orden as OrdenDTO
from .mapeadores import MapeadorOrden
from uuid import UUID

class RepositorioProductosSQLite(RepositorioProductos):

    def obtener_por_id(self, id: UUID) -> Producto:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Producto]:
        fecha_creacion="2023-01-31 18:53:59.264253"
        fecha_actualizacion ="2023-01-31 18:53:59.264253"
        nombre="Test 2"
        precio="150"
        producto = Producto(fecha_creacion, fecha_actualizacion, nombre, precio)
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

    def obtener_por_id(self, id: UUID) -> ov.Orden:
        orden_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        print("RepositorioOrdenesSQLite obtener_por_id ", orden_dto)
        return self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())

    def obtener_todos(self) -> list[ov.Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        print("------",orden)
        orden_dto = self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())
        db.session.add(orden_dto)
        db.session.commit()
        print("---*****---",orden)

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError