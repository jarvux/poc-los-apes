from pulsar.schema import *
from dataclasses import dataclass, field
from entrega.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoEntregaOrdenPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoEntregarOrden(ComandoIntegracion):
    data = ComandoEntregaOrdenPayload()
