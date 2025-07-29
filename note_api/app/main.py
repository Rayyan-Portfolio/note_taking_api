# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Note Taking API is Live!"}


from fastapi import FastAPI
from app.routes import note, tag

app = FastAPI()

app.include_router(note.router)
app.include_router(tag.router)
