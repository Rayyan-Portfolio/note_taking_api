# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Note Taking API is Live!"}


from fastapi import FastAPI
from app.routes import note, tag ,user, auth

app = FastAPI()

app.include_router(note.router)
app.include_router(tag.router)
# app.include_router(user.router)
app.include_router(auth.router)
