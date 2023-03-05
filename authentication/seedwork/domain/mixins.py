from .rules import ReglaNegocio
from .exceptions import ReglaNegocioExcepcion


class ValidarReglasMixin:
    def validar_regla(self, regla: ReglaNegocio):
        if not regla.es_valido():
            raise ReglaNegocioExcepcion(regla)
