from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import role_routes

app = FastAPI()

app.include_router(role_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
