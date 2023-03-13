from pulsar.schema import *
from .utils import time_millis
import uuid

class OrdenDespachada(Record):
    id = String()
    id_despacho = String()
    orden_id = String()
    fecha_creacion = Long()
 
class DespachoRevertido(Record):
    id = String()
    id_despacho = String()
    orden_id = String()
    fecha_actualizacion = Long()

class EventoDespacho(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoDespacho")
    datacontenttype = String()
    service_name = String(default="despacho.entregadelosalpes")
    orden_despachada = OrdenDespachada
    pago_revertido = DespachoRevertido

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)