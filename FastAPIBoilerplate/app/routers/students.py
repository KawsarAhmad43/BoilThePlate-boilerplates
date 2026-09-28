from fastapi import APIRouter, HTTPException, Depends
# Depends is used to inject the database session into the route.

from sqlalchemy.orm import Session
# Session type for type hinting our database connection.

from typing import List

from app.schemas.student import Student, StudentCreate, StudentUpdate
# importing our Pydantic models for request body validation

from app.database.database import get_db
from app.database.models import DBStudent
# importing DB tools instead of the old fake list

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/", response_model=Student, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Converting Pydantic model to SQLAlchemy model
    db_student = DBStudent(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/", response_model=List[Student])
def get_all_students(db: Session = Depends(get_db)):
    return db.query(DBStudent).all()

@router.get("/{student_id}", response_model=Student)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, updated_data: StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    # exclude_unset=True ensures we only update fields the user actually sent
    update_data_dict = updated_data.model_dump(exclude_unset=True)
    
    for key, value in update_data_dict.items():
        setattr(db_student, key, value)
        
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully", "deleted_id": student_id}
