from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.models import ModeloBase

class Comerciante(ModeloBase):
    __tablename__ = "comerciantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String)
    telefono: Mapped[str] = mapped_column(String)
    direccion: Mapped[str] = mapped_column(String)