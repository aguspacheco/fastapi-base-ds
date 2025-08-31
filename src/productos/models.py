from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from enum import auto, StrEnum
from src.models import ModeloBase

class TipoProducto(StrEnum):
    ALAPIEDRA = auto()
    HORNO = auto()
    ALMOLDE = auto()
    MASAMADRE = auto()
    FINITA = auto()

class Producto(ModeloBase):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[TipoProducto] = mapped_column(String) 
 