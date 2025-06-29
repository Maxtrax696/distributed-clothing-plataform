from fastapi import FastAPI
from app.controllers import profile_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(profile_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Profile Service is running"}