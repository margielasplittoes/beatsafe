from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import beats

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title ="Beatsafe API")

app.include_router(beats.router)

@app.get("/")
def root():
    return{"status": "Beatsafe backend running"}
