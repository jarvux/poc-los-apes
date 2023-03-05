from authentication.seedwork.application.services import Service
from authentication.modules.auth.domain.entities import User
from authentication.modules.auth.domain.factories import UserFactory
from authentication.modules.auth.infrastructure.factories import FabricaRepositorio
from authentication.modules.auth.infrastructure.repositories import RepositoryUsers

from .dto import UserDTO, LoginDTO
from .mappers import MapperUser

from flask_jwt_extended import create_access_token


class ServiceUser(Service):

    def __init__(self):
        self._factory_repository: FabricaRepositorio = FabricaRepositorio()
        self._factory_users: UserFactory = UserFactory()

    @property
    def factory_repository(self):
        return self._factory_repository

    @property
    def factory_users(self):
        return self._factory_users

    def create_user(self, user_dto: UserDTO) -> UserDTO:
        us: User = self.factory_users.create_object(user_dto, MapperUser())

        repo = self.factory_repository.create_object(RepositoryUsers.__class__)
        repo.add(us)

        return self.factory_users.create_object(us, MapperUser())

    def get_user(self, login_dto: LoginDTO) -> LoginDTO:
        repo = self.factory_repository.create_object(RepositoryUsers.__class__)
        return repo.get_user(login_dto.name, login_dto.password)
        # .__dict__


class ServiceToken(Service):

    def create_token(self, user_dto: UserDTO) -> UserDTO:
        token = create_access_token(identity=user_dto.name)
        return token
