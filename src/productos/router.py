from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_session
from . import services, schemas
from .constants import ROUTER_PREFIX
from .exceptions import ProductoNotFound

router = APIRouter(prefix=ROUTER_PREFIX, tags=["productos"])

@router.get("/", response_model=list[schemas.ProductoOut])
def list_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return services.get_all(db, skip=skip, limit=limit)

@router.get("/{producto_id}", response_model=schemas.ProductoOut)
def get_producto(producto_id: int, db: Session = Depends(get_session)):
    obj = services.get_by_id(db, producto_id)
    if not obj:
        raise ProductoNotFound()
    return obj

@router.post("/", response_model=schemas.ProductoOut, status_code=status.HTTP_201_CREATED)
def create_producto(data: schemas.ProductoCreate, db: Session = Depends(get_session)):
    return services.create(db, data)

@router.put("/{producto_id}", response_model=schemas.ProductoOut)
def update_producto(producto_id: int, data: schemas.ProductoUpdate, db: Session = Depends(get_session)):
    obj = services.update(db, producto_id, data)
    if not obj:
        raise ProductoNotFound()
    return obj

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_producto(producto_id: int, db: Session = Depends(get_session)):
    ok = services.delete(db, producto_id)
    if not ok:
        raise ProductoNotFound()
    return None
