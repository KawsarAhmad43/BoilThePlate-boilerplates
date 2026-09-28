from fastapi import FastAPI
# initializing the main app object

from app.routers import students
# importing the students router to plug it in

from app.database.database import engine
from app.database import models
# Importing engine and models to auto-create tables

# Creates the tables in MySQL automatically if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Project",
    description="CRUD application using APIRouter and MySQL.",
    version="1.0.0"
)

app.include_router(students.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI project is running. Visit /docs for the Swagger UI."}
