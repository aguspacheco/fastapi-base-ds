from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.comerciantes.models import Comerciante
from src.comerciantes import schemas, exceptions

def crear_comerciante(db: Session, comerciante: schemas.ComercianteCreate) -> schemas.Comerciante:
    _comerciante = Comerciante(**comerciante.model_dump())
    db.add(_comerciante)
    db.commit()
    db.refresh(_comerciante)
    return _comerciante


def listar_comerciantes(db: Session) -> List[schemas.Comerciante]:
    return db.scalars(select(Comerciante)).all()

def leer_comerciante(db: Session, comerciante_id: int) -> schemas.Comerciante:
    db_comerciante = db.scalar(select(Comerciante).where(Comerciante.id == comerciante_id))
    if db_comerciante is None:
        raise exceptions.ComercianteNoEncontrada()
    return db_comerciante

def eliminar_comerciante(db: Session, comerciante_id: int) -> schemas.Comerciante:
    db_comerciante = leer_comerciante(db, comerciante_id)
    db.delete(db_comerciante)
    db.commit()
    return db_comerciante