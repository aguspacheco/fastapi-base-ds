from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from database import Base  

class Comerciante(Base):
    __tablename__ = "comerciantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    telefono = Column(String(50), nullable=True)
    direccion = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, server_default="1")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
