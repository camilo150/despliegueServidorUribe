import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from app.api.models.tablas import Base
from app.database.connection import engine
from app.api.endpoints import seresvivos


# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return RedirectResponse("/docs")

# Incluir rutas
app.include_router(seresvivos.router)
