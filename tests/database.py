import os
import pytest
from dotenv import load_dotenv
from typing import Generator
from sqlalchemy import StaticPool, create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from src.main import app
from src.database import get_db
from src.models import ModeloBase
from src.productos.services import crear_producto
from src.comerciantes.services import crear_comerciante
from src.productos.schemas import ProductoCreate
from src.comerciantes.schemas import ComercianteCreate
from src.productos.models import TipoProducto

load_dotenv()

# creamos una db para testing
DATABASE_URL = os.getenv("DB_URL_TEST")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    # utilizaremos esta funcion para "pisar" la que definimos en src/database.py.
    db = TestingSessionLocal()
    # Para usar restricciones de FK en SQLite, debemos habilitar la siguiente opción:
    db.execute(text("PRAGMA foreign_keys = ON"))
    try:
        print("Using test DB!")
        yield db
    finally:
        db.close()

# forzamos a fastapi para que utilice la db para testing.
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def session() -> Generator[Session, None, None]:
    # Creamos las tablas en la db de pruebas
    ModeloBase.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    # Para usar restricciones de FK en SQLite, debemos habilitar la siguiente opción:
    db.execute(text("PRAGMA foreign_keys = ON"))

    # aqui podemos crear instancias de objetos para hacer tests
    # haciendo uso de las funciones "create_<clase>" de services y los schemas <Clase>Create.
    comerciante_1 = crear_comerciante(db, ComercianteCreate(nombre="Juan", email="juan.perez@gmail.com"))
    comerciante_2 = crear_comerciante(
        db, ComercianteCreate(nombre="Ana", email="ana.dominguez@gmail.com")
    )
    producto_1 = crear_producto(db, ProductoCreate(nombre="pizza muzzarela", tutor_id=comerciante_1.id))
    producto_2 = crear_producto(db, ProductoCreate(nombre="Pizza anana", tutor_id=comerciante_1.id))
    producto_3 = crear_producto(db, ProductoCreate(nombre="Pizza fugazzeta", tutor_id=comerciante_2.id))

    db.add_all(
        [
            comerciante_1,
            comerciante_2,
            producto_1,
            producto_2,
            producto_3
        ]
    )
    db.commit()

    yield db

    db.close()
    ModeloBase.metadata.drop_all(bind=engine)
