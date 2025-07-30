from fastapi import FastAPI
from app.routes import note, tag ,user, auth

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running ✅. Only added this for deployment. now add '/docs' to access api endpoints"}

app.include_router(note.router)
app.include_router(tag.router)
app.include_router(auth.router)
