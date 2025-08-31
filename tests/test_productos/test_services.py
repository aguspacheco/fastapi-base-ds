import pytest 
from sqlalchemy.orm import Session
from src import productos
from src.productos.services import listar_productos
from tests.database import session

def test_listar_productos(session: Session) -> None:
    productos = listar_productos(session)
    assert len(productos) == 3