from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.staticfiles import StaticFiles
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

=======
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from fastapi.staticfiles import StaticFiles
>>>>>>> qa

app = FastAPI()
app.include_router(router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
<<<<<<< HEAD
)
=======
)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
>>>>>>> qa
