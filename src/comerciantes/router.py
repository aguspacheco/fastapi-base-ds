from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_session  # del proyecto base
from . import services, schemas
from .constants import ROUTER_PREFIX
from .exceptions import ComercianteNotFound, EmailAlreadyExists

router = APIRouter(prefix=ROUTER_PREFIX, tags=["comerciantes"])

@router.get("/", response_model=list[schemas.ComercianteOut])
def list_comerciantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return services.get_all(db, skip=skip, limit=limit)

@router.get("/{comerciante_id}", response_model=schemas.ComercianteOut)
def get_comerciante(comerciante_id: int, db: Session = Depends(get_session)):
    obj = services.get_by_id(db, comerciante_id)
    if not obj:
        raise ComercianteNotFound()
    return obj

@router.post("/", response_model=schemas.ComercianteOut, status_code=status.HTTP_201_CREATED)
def create_comerciante(data: schemas.ComercianteCreate, db: Session = Depends(get_session)):
    if services.get_by_email(db, data.email):
        raise EmailAlreadyExists()
    return services.create(db, data)

@router.put("/{comerciante_id}", response_model=schemas.ComercianteOut)
def update_comerciante(comerciante_id: int, data: schemas.ComercianteUpdate, db: Session = Depends(get_session)):
    obj = services.update(db, comerciante_id, data)
    if not obj:
        raise ComercianteNotFound()
    return obj

@router.delete("/{comerciante_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comerciante(comerciante_id: int, db: Session = Depends(get_session)):
    ok = services.delete(db, comerciante_id)
    if not ok:
        raise ComercianteNotFound()
    return None
