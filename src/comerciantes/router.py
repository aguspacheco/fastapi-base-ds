from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db  
from src.comerciantes import schemas, services

router = APIRouter(prefix="/comerciantes", tags=["comerciantes"])

@router.post("/", response_model=schemas.Comerciante)
def create_comerciante(comerciante: schemas.ComercianteCreate, db: Session = Depends(get_db)):
    return services.crear_comerciante(db, comerciante)

@router.get("/", response_model=list[schemas.Comerciante])
def read_comerciantes(db: Session = Depends(get_db)):
    return services.listar_comerciantes(db)

@router.get("/{comerciante_id}", response_model=schemas.Comerciante)
def read_comerciante(comerciante_id: int, db: Session = Depends(get_db)):
    return services.leer_comerciante(db, comerciante_id)

#@router.put("/{comerciante_id}", response_model=schemas.Comerciante)
#def update_comerciante(comerciante_id: int, comerciante: schemas.ComercianteUpdate, db: Session = Depends(get_db)):
#    return services.modificar_comerciante(db, comerciante_id, comerciante)

@router.delete("/{comerciante_id}", response_model=schemas.Comerciante)
def delete_comerciante(comerciante_id: int, db: Session = Depends(get_db)):
    return services.eliminar_comerciante(db, comerciante_id)
