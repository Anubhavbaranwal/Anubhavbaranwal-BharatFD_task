from fastapi import APIRouter, Query, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import faq
from ..schema import FAQCreate, FAQUpdate

router = APIRouter(
    tags=["FAQS"],
    prefix="/faq"
)

@router.get("/")
def read_faqs(lang: str = Query('en'), db: Session = Depends(get_db)):
    return faq.get_faqs(db, lang)

@router.get("/{faq_id}")
def read_faq(faq_id: int, lang: str = Query('en'), db: Session = Depends(get_db)):
    db_faq = faq.get_faq(db, faq_id, lang)
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return db_faq

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_faq(faq_data: FAQCreate, db: Session = Depends(get_db)):
    return faq.create_faq(db, faq_data)

@router.put("/{faq_id}")
def update_faq(faq_id: int, faq_data: FAQUpdate, db: Session = Depends(get_db)):
    db_faq = faq.update_faq(db, faq_id, faq_data)
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return db_faq

@router.delete("/{faq_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    db_faq = faq.delete_faq(db, faq_id)
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)