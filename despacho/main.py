from fastapi import FastAPI

import asyncio
import time
import traceback
import uvicorn

from pydantic import BaseSettings
from typing import Any

from .eventos import EventoDespacho, DespachoRevertido, OrdenDespachada
from .comandos import ComandoDespacharOrden, ComandoRevertirDespacharOrden, RevertirDespachoPayload, DespacharOrdenPayload
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador

from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Despacho Orden EntregaDelosAlpes"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-despacho", "sub-despachos", EventoDespacho))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-despachar-orden", "sub-com-despachos-orden", ComandoDespacharOrden))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-revertir-despacho", "sub-com-despachos-revertir", ComandoRevertirDespacharOrden))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()
