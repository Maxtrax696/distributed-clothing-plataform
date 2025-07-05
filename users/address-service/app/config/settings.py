from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
