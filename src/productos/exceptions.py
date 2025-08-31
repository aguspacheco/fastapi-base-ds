from typing import List
from src.productos.constants import ErrorCode
from src.exceptions import NotFound, BadRequest

class ProductoNoEncontrado(NotFound):
    DETAIL = ErrorCode.PRODUCTO_NO_ENCONTRADO

class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.PRODUCTO_DUPLICADO

class TipoProductoInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TIPO_PRODUCTO_INVALIDO} {posibles_tipos}"
        super().__init__(message)   
