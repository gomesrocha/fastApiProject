from dotenv import load_dotenv
from functools import lru_cache
from fastapi import Depends, FastAPI
from schema.settings import Settings
from routers.api_logistica import router as entregaapi

load_dotenv()

app = FastAPI()
@lru_cache()
def get_settings():
    return Settings()

@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "idapi": settings.idapi,
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(entregaapi, prefix="/v1", tags=["v1"])