from pulsar.schema import *
from entrega.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from entrega.seedwork.infraestructura.utils import time_millis
import uuid

class OrdenCreadaPayload(Record):
    id_orden: uuid.UUID = None
    id_cliente: uuid.UUID = None
    items: str = None
    estado: str = None
    fecha_creacion: str = None

class EventoOrdenCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = OrdenCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
   