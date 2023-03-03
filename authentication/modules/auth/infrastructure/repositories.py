
from authentication.modules.auth.application.mappers import MapperUser
from authentication.modules.auth.domain.factories import UserFactory
from authentication.modules.auth.domain.repositories import RepositoryUsers
from authentication.modules.auth.domain.entities import User
from .dto import Users
from authentication.config.db import db
class RepositoryUsersSQLite(RepositoryUsers):

    def __init__(self):
        self._factory_users: UserFactory = UserFactory()

    @property
    def factory_users(self):
        return self._factory_users

    def obtener_por_id(self, id: str) -> User:
         # TODO
        raise NotImplementedError
        #reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        #return self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[User]:
        # TODO
        raise NotImplementedError

    def add(self, user: User):
        reserva_dto = self.factory_users.create_object(user, MapperUser())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, user: User):
        # TODO
        raise NotImplementedError

    def eliminar(self, iser_id: str):
        # TODO
        raise NotImplementedError