from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas, models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit")
def submit_form941(form: schemas.Form941Create, db: Session = Depends(get_db)):
    db_form = models.Form941(**form.dict())
    db.add(db_form)
    db.commit()
    return {"message": "Form 941 submitted", "id": db_form.id}

@router.get("/all")
def get_all_forms(db: Session = Depends(get_db)):
    return db.query(models.Form941).all()