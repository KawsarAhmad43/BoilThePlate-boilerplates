from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.database import Base
# Importing Base from our database config so SQLAlchemy knows this is a table

class DBStudent(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    department = Column(String(100))
    cgpa = Column(Float)
    is_active = Column(Boolean, default=True)
