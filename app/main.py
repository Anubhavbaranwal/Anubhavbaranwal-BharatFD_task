from fastapi import FastAPI, Query
from sqlalchemy.orm import Session
from .models import FAQ, Base
from .database import engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/api/faqs/")
def read_faqs(lang: str = Query('en')):
    db: Session = SessionLocal()
    faqs = db.query(FAQ).all()
    translated_faqs = [
        {
            "question": faq.get_translation(lang)[0],
            "answer": faq.get_translation(lang)[1]
        }
        for faq in faqs
    ]
    return translated_faqs