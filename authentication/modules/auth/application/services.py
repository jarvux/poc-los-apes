
from authentication.modules.auth.domain.repositories import RepositoryUsers
from authentication.seedwork.application.services import Service
from authentication.modules.auth.application.dto import UserDTO
from authentication.modules.auth.application.mappers import MapperUser
from authentication.modules.auth.domain.entities import User

from authentication.modules.auth.infrastructure.factories import FabricaRepositorio
from authentication.modules.auth.domain.factories import UserFactory

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
        us : User = self.factory_users.create_object(user_dto, MapperUser())
        
        repo = self.factory_repository.create_object(RepositoryUsers.__class__)
        repo.add(us)
        
        return self.factory_users.create_object(us, MapperUser())