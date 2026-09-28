from pydantic import BaseModel, ConfigDict
# Using BaseModel so we don't have to manually write if-else type checkers for every field.

from typing import Optional
# Optional is so a field can be null. Super useful for the PUT request when updating just one field.

class StudentBase(BaseModel):
    name: str
    department: str
    cgpa: float
    is_active: bool = True

class StudentCreate(StudentBase):
    pass
    # We don't ask the user to provide an ID when creating, the DB will auto-generate it!

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    cgpa: Optional[float] = None
    is_active: Optional[bool] = None

class Student(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
    # This tells Pydantic to read the data even if it's an SQLAlchemy model (not just a python dictionary)
