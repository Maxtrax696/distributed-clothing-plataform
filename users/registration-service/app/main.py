from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
=======
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
>>>>>>> qa
from fastapi.responses import RedirectResponse
from app.routes import router

app = FastAPI()
<<<<<<< HEAD

# Cargar rutas del backend
app.include_router(router)

# Redirigir raíz `/` hacia el formulario
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

# Servir archivos estáticos desde /static
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# CORS
=======
app.include_router(router)

>>>>>>> qa
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
<<<<<<< HEAD
=======

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Redirigir la raíz a index.html
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")
>>>>>>> qa
