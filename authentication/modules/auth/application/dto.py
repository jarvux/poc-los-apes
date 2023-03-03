from dataclasses import dataclass, field
from authentication.seedwork.application.dto import DTO
    
@dataclass(frozen=True)
class UserDTO(DTO):
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    password: str = field(default_factory=str)    
    role: int = field(default_factory=int)
    
