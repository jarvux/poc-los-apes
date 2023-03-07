from pydispatch import dispatcher

from .handlers import HandlerOrdenIntegracion

from entregadelosalpes.modulos.orden.dominio.eventos import OrdenCreada
print("XXXXXXXX.......HANDLER")
dispatcher.connect(HandlerOrdenIntegracion.handle_orden_creada, signal=f'{OrdenCreada.__name__}Integracion')
