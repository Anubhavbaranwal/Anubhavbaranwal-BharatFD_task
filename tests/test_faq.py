import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import FAQ

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_faq(test_db):
    response = client.post("/faq/", json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework."})
    assert response.status_code == 201
    assert response.json()["question"] == "What is FastAPI?"

def test_get_faq(test_db):
    response = client.get("/faq/1?lang=en")
    assert response.status_code == 200
    assert response.json()["question"] == "What is FastAPI?"

def test_get_faqs(test_db):
    response = client.get("/faq/?lang=en")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_faq(test_db):
    response = client.put("/faq/1", json={"question": "What is FastAPI?", "answer": "FastAPI is a modern, fast web framework."})
    assert response.status_code == 200
    assert response.json()["answer"] == "FastAPI is a modern, fast web framework."

def test_delete_faq(test_db):
    response = client.delete("/faq/1")
    assert response.status_code == 200
    assert response.json()["message"] == "FAQ with ID 1 successfully deleted"