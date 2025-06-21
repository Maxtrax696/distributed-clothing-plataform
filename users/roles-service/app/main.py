from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # ← añade esto
from app.routes import router

app = FastAPI()

app.include_router(router)

# Servir archivos estáticos desde / (ej: index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
