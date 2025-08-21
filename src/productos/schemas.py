from pydantic import BaseModel, Field

class ProductoBase(BaseModel):
    precio: float = Field(..., gt=0, description="Precio del producto, debe ser mayor a 0")
    masa: bool = Field(..., description="Si el producto tiene masa o no")
    sabores: str = Field(..., min_length=1, description="Sabores del producto")
    img: str | None = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    precio: float | None = Field(None, gt=0)
    masa: bool | None = None
    sabores: str | None = None
    img: str | None = None

class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True  
