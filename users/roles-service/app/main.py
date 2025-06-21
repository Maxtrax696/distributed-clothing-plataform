from fastapi import FastAPI
from app.routes import router


app = FastAPI()


@app.get("/")
def root():
    return {"message": "roles-service is running"}


app.include_router(router)
