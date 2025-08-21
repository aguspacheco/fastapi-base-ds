import pytest
from sqlalchemy.orm import Session
from src.comerciantes.services import listar_comerciantes
from tests.database import session

def test_listar_comerciantes(session: Session) -> None:
    comerciantes = listar_comerciantes(session)
    assert len(comerciantes) == 3