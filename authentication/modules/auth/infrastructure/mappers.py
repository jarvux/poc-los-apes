from authentication.seedwork.domain.repositories import Mapper

# from .dto import Users
from authentication.modules.auth.domain.entities import User
from .dto import Users as UserDTO


class MapperUsers(Mapper):

    def get_type(self) -> type:
        return User.__class__

    def entity_to_dto(self, entity: User) -> UserDTO:
        usr_dto = UserDTO()
        usr_dto.id = str(entity.id)
        usr_dto.name = str(entity.name)
        usr_dto.password = str(entity.password)
        usr_dto.role = str(entity.role)
        return usr_dto

    def dto_to_entity(self, dto: UserDTO) -> User:
        usr = User(dto.id, dto.name, dto.password, dto.role)
        return usr
