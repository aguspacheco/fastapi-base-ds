from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base  

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    precio = Column(Float, nullable=False)
    masa = Column(Boolean, nullable=False, default=False)
    sabores = Column(String(255), nullable=False)
    img = Column(String(255), nullable=True)  
