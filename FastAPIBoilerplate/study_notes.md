FastAPI personal study notes

What is FastAPI and why use it?
I checked the documentation, and it says it's built on Starlette and Pydantic.
The best part is type hints. Python is normally dynamically typed, but here if someone sends a string instead of an int, FastAPI automatically throws an error. I don't have to write manual if-else checks to validate data. Also the swagger docs at /docs are generated automatically which saves a lot of time testing.

Project Structure (Refactored)
Initially, I dumped everything into one main.py file. But I learned that in the real world, code needs to be modular. So I broke it down:
- app/main.py: The main engine that initializes FastAPI.
- app/routers/: This is where APIRouter lives. Instead of @app.get, we use @router.get to group endpoints.
- app/schemas/: This holds the Pydantic BaseModels (like Student and StudentUpdate) for data validation.
- app/database/: For now, just holds my fake list DB to simulate data storage.

Pydantic Models
Why are we using classes that inherit from BaseModel? It's for data validation. When a POST request comes with JSON, FastAPI passes that JSON to the Pydantic model. If they match, it creates a Python object. If not, it returns a 422 error. It works like a DTO.

HTTP Methods 
GET: fetch data.
POST: send new data to the server.
PUT: update a resource.
DELETE: remove a resource.

Fake Database
I'm using a simple Python list as a database for now. It's fast and needs no setup, but it's volatile so data is gone when the server restarts. Good enough for proof of concept.

Path vs Query Parameters
Path Parameter: /items/{item_id}. It's mandatory. 
Query Parameter: /items?limit=10. This is usually optional, used for sorting or filtering.

Mistakes I made while building this
- I forgot to return the updated item in the PUT method at first. Just updating the list isn't enough, the client needs the final state to know it worked.
- The item_id in my model is an integer, but it's not the list index. I had to use a loop to actually find the correct item to update/delete instead of just doing list[id].
- When moving from one file to a modular folder structure, I had to remember to change the startup command from `uvicorn main:app` to `uvicorn app.main:app`.

Next Steps
Try connecting a real database, maybe SQLite.
Learn about Dependency Injection.
Try async/await properly since the fake DB is synchronous right now.
