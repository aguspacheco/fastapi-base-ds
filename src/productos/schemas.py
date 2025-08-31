from pydantic import BaseModel, field_validator
from src.productos.models import TipoProducto
from src.productos import exceptions

class ProductoBase(BaseModel):
    nombre: str
    tipo: TipoProducto

    @field_validator("tipo", mode="before")
    @classmethod
    def is_valid_tipo_producto(cls, v: str) -> str:
        if v.lower() not in TipoProducto:
            raise exceptions.TipoProductoInvalido(list(TipoProducto))
        return v.lower()

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    tipo: TipoProducto
    model_config = {"from_attributes": True} 

class ProductoDelete(ProductoBase):
    id: int