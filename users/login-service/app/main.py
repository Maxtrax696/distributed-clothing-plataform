from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from app.routes import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
=======
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()
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
app.include_router(router)
=======
>>>>>>> qa
app.mount("/", StaticFiles(directory="static", html=True), name="static")
