from authentication.seedwork.application.dto import Mapper as AppMap
from authentication.seedwork.domain.repositories import Mapper as RepMap
from authentication.modules.auth.domain.entities import User
from .dto import UserDTO
from .dto import LoginDTO


class MapperAuthDTOJson(AppMap):

    def ext_to_dto(self, external: dict) -> UserDTO:
        return UserDTO(
            name=external.get('name'),
            password=external.get('password'),
            role=external.get('role'))

    def dto_to_ext(self, dto: UserDTO) -> dict:
        return dto.__dict__


class MapperUser(RepMap):

    def get_type(self) -> type:
        return User.__class__

    def entity_to_dto(self, entidad: User) -> UserDTO:
        return UserDTO(str(entidad.id), str(entidad.name), str(entidad.password), int(entidad.role))

    def dto_to_entity(self, dto: UserDTO) -> User:
        return User(dto.id, dto.name, dto.password, dto.role)


class MapperLoginDTOJson(AppMap):
    def ext_to_dto(self, external: dict) -> LoginDTO:
        return LoginDTO(name=external.get('name'), password=external.get('password'))

    def dto_to_ext(self, dto: LoginDTO) -> dict:
        return dto.__dict__
