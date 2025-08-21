from pydantic import BaseModel, EmailStr, Field

class ComercianteBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    telefono: str | None = None
    direccion: str | None = None
    activo: bool = True

class ComercianteCreate(ComercianteBase):
    pass

class ComercianteUpdate(BaseModel):
    nombre: str | None = Field(None, min_length=1, max_length=200)
    email: EmailStr | None = None
    telefono: str | None = None
    direccion: str | None = None
    activo: bool | None = None

class ComercianteOut(ComercianteBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2: permite mapear desde ORM
