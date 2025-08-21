from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi import status
from tests.database import app, session


client = TestClient(app)


def test_read_comerciantes(session: Session) -> None:
    response = client.get(f"/comerciantes")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3