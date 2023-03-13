from pulsar.schema import *
from .utils import time_millis
import uuid

class DespacharOrdenPayload(Record):
    id_despacho = String()
    orden_id = String()
    fecha_creacion = Long()
 
class RevertirDespachoPayload(Record):
    id = String()
    id_despacho = String()
    orden_id = String()

class ComandoDespacharOrden(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoDespacharOrden")
    datacontenttype = String()
    service_name = String(default="despacho.entregadelosalpes")
    data = DespacharOrdenPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirDespacharOrden(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoRevertirDespacharOrden")
    datacontenttype = String()
    service_name = String(default="pagos.aeroalpes")
    data = RevertirPagoPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)