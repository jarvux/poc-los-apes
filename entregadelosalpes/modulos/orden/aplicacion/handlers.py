from entregadelosalpes.modulos.orden.dominio.eventos import OrdenCreada
from entregadelosalpes.seedwork.aplicacion.handlers import Handler
from entregadelosalpes.modulos.orden.infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):

    @staticmethod
    def handle_orden_creada(evento):
        print("HandlerOrdenIntegracion")
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')

    