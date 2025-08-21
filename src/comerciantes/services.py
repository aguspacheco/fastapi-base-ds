from sqlalchemy.orm import Session
from . import models, schemas

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comerciante).offset(skip).limit(limit).all()

def get_by_id(db: Session, comerciante_id: int):
    return db.query(models.Comerciante).filter(models.Comerciante.id == comerciante_id).first()

def get_by_email(db: Session, email: str):
    return db.query(models.Comerciante).filter(models.Comerciante.email == email).first()

def create(db: Session, data: schemas.ComercianteCreate):
    obj = models.Comerciante(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, comerciante_id: int, data: schemas.ComercianteUpdate):
    obj = get_by_id(db, comerciante_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, comerciante_id: int):
    obj = get_by_id(db, comerciante_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
