from dataclasses import dataclass, field
from authentication.modules.auth.infrastructure.repositories import RepositoryUsersSQLite
from authentication.seedwork.domain.exceptions import ExcepcionFabrica
from authentication.seedwork.domain.factories import Fabrica
from authentication.seedwork.domain.repositories import Repository
from authentication.modules.auth.domain.repositories import RepositoryUsers


@dataclass
class FabricaRepositorio(Fabrica):

    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == RepositoryUsers.__class__:
            return RepositoryUsersSQLite()
        else:
            raise ExcepcionFabrica()
