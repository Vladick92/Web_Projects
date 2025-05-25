from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine,Base,db_dependency
from app.models import *
from .routers import user_router,card_router,real_estate_router,banker_router,deposit_router,credit_router,auth

app=FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router=auth.router)
app.include_router(router=user_router.router)
app.include_router(router=card_router.router)
app.include_router(router=real_estate_router.router)
app.include_router(router=banker_router.router)
app.include_router(router=deposit_router.router)
app.include_router(router=credit_router.router)