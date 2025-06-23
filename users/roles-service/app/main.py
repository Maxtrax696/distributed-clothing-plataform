from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.staticfiles import StaticFiles  # ← añade esto
from app.routes import router

app = FastAPI()

app.include_router(router)

# Servir archivos estáticos desde / (ej: index.html)
=======
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

>>>>>>> qa
app.mount("/", StaticFiles(directory="static", html=True), name="static")
