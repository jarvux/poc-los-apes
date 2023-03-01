from dataclasses import dataclass, field
import uuid

@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    fecha_creacion: datetime = field(default=datetime.now())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4