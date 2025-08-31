from pydantic import BaseModel, EmailStr


class ComercianteBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str | None = None
    direccion: str | None = None

class ComercianteCreate(ComercianteBase):
    pass

class ComercianteUpdate(ComercianteBase):
    pass

class Comerciante(ComercianteBase):
    id: int
    model_config = {"from_attributes": True}
