from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine,Base
from . import ranger_router

app=FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router=ranger_router.router)
