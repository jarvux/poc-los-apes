from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Orden(_message.Message):
    __slots__ = ["fecha_actualizacion", "fecha_creacion", "id", "items"]
    FECHA_ACTUALIZACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CREACION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    fecha_actualizacion: str
    fecha_creacion: str
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Producto]
    def __init__(self, id: _Optional[str] = ..., fecha_creacion: _Optional[str] = ..., fecha_actualizacion: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Producto, _Mapping]]] = ...) -> None: ...

class Producto(_message.Message):
    __slots__ = ["fecha_actualizacion", "fecha_creacion", "nombre", "precio"]
    FECHA_ACTUALIZACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CREACION_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    PRECIO_FIELD_NUMBER: _ClassVar[int]
    fecha_actualizacion: str
    fecha_creacion: str
    nombre: str
    precio: str
    def __init__(self, fecha_creacion: _Optional[str] = ..., fecha_actualizacion: _Optional[str] = ..., nombre: _Optional[str] = ..., precio: _Optional[str] = ...) -> None: ...

class QueryOrden(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RespuestaOrden(_message.Message):
    __slots__ = ["mensaje", "orden"]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    ORDEN_FIELD_NUMBER: _ClassVar[int]
    mensaje: str
    orden: Orden
    def __init__(self, mensaje: _Optional[str] = ..., orden: _Optional[_Union[Orden, _Mapping]] = ...) -> None: ...
