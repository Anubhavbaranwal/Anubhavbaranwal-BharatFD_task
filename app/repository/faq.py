from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models import FAQ
from ..schema import FAQCreate, FAQUpdate

def get_faqs(db: Session, lang: str = 'en'):
    try:
        faq_records = db.query(FAQ).all()
        if not faq_records:
            raise HTTPException(status_code=404, detail="No FAQs found")

        translated_faqs = [
            {"id": faq.id, "question": faq.get_translation(lang)[0], "answer": faq.get_translation(lang)[1]}
            for faq in faq_records
        ]
        return translated_faqs

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def get_faq(db: Session, faq_id: int, lang: Optional[str] = 'en'):
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail=f"FAQ with ID {faq_id} not found")
    
    question, answer = faq.get_translation(lang)
    return {"id": faq.id, "question": question, "answer": answer}

def create_faq(db: Session, faq: FAQCreate):
    try:
        db_faq = FAQ(**faq.model_dump())
        db.add(db_faq)
        db.commit()
        db.refresh(db_faq)
        return db_faq

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating FAQ: {str(e)}")
    
def update_faq(db: Session, faq_id: int, faq: FAQUpdate):
    db_faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not db_faq:
        raise HTTPException(status_code=404, detail=f"FAQ with ID {faq_id} not found")

    try:
        update_data = faq.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_faq, key, value)

        db.commit()
        db.refresh(db_faq)
        return db_faq

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating FAQ: {str(e)}")

def delete_faq(db: Session, faq_id: int):
    db_faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not db_faq:
        raise HTTPException(status_code=404, detail=f"FAQ with ID {faq_id} not found")

    try:
        db.delete(db_faq)
        db.commit()
        return {"message": f"FAQ with ID {faq_id} successfully deleted"}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting FAQ: {str(e)}")
