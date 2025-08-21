from sqlalchemy.orm import Session
from . import models, schemas

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).offset(skip).limit(limit).all()

def get_by_id(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def create(db: Session, data: schemas.ProductoCreate):
    obj = models.Producto(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, producto_id: int, data: schemas.ProductoUpdate):
    obj = get_by_id(db, producto_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, producto_id: int):
    obj = get_by_id(db, producto_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
