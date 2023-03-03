
from .exceptions import TipoObjetoNoExisteEnDominioVuelosExcepcion
from .entities import User
from dataclasses import dataclass
from authentication.seedwork.domain.entities import Entidad
from authentication.seedwork.domain.repositories import Mapper
from authentication.seedwork.domain.factories import Fabrica


@dataclass
class _FactoryUser(Fabrica):
    def crear_objeto(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entidad):
            return mapper.entidad_a_dto(obj)
        else:
            user: User = mapper.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return user
        
@dataclass
class UserFactory(Fabrica):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if mapper.obtener_tipo() == User.__class__:
            factory_user = _FactoryUser()
            return factory_user.crear_objeto(obj, mapper)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()