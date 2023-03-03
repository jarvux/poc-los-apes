from authentication.modules.auth.application.dto import UserDTO
from authentication.seedwork.application.dto import Mapper as AppMap
from authentication.seedwork.domain.repositories import Mapper as RepMap
from authentication.modules.auth.domain.entities import User

class MapperAuthDTOJson(AppMap):
        
    def ext_to_dto(self, external: dict) -> UserDTO:
        user_DTO = UserDTO()    
        user_DTO.id = external.get('id')
        user_DTO.name = external.get('name')
        user_DTO.password = external.get('password')
        user_DTO.role = external.get('role')  
        return user_DTO
    
    def dto_to_ext(self, dto: UserDTO) -> dict:
        return dto.__dict__
    
    
class MapperUser(RepMap):
    
    def get_type(self) -> type:
        return User.__class__
    
    def entity_to_dto(self, entidad: User) -> UserDTO:             
        _id = str(entidad.id)
        name = str(entidad.name)
        password = str(entidad.password)
        role = int(entidad.role)

        return UserDTO(_id, name, password, role)

    def dto_to_entity(self, dto: UserDTO) -> User:
        usr = User()
        usr.id = dto.id
        usr.name = dto.name
        usr.password = dto.password
        usr.role = dto.role
        
        return usr