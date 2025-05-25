from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine,db_dependency
from . import models 
from .routers import books,categories,items,todos,users

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(books.router)
app.include_router(categories.router)
app.include_router(items.router)
app.include_router(todos.router)
app.include_router(users.router)