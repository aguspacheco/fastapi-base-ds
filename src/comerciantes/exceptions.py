from src.comerciantes.constants import ErrorCode
from src.exceptions import NotFound, BadRequest

class ComercianteNoEncontrada(NotFound):
    DETAIL = ErrorCode.COMERCIANTE_NO_ENCONTRADA

class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO


class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO
