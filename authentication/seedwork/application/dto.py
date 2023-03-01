from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class DTO():
    ...


class Mapper(ABC):
    @abstractmethod
    def ext_to_dto(self, ext: any) -> DTO:
        ...

    @abstractmethod
    def dto_to_ext(self, dto: DTO) -> any:
        ...
