from fastapi import FastAPI
from app.routers import endpoints

app = FastAPI()
# skyrim_potions/app/routers/endpoints.py
app.include_router(endpoints.router)