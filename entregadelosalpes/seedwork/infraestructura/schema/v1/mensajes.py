import uuid

from pulsar.schema import *

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()