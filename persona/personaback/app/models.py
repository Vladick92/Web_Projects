from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Users(Base):
    __tablename__ = 'users'
    user_uuid = Column(UUID(as_uuid=True),primary_key=True,index=True,unique=True,server_default=text("gen_random_uuid()"))
    username = Column(String, index=True, nullable=False)
    user_pass = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    todos=relationship("Todo_items",back_populates="user")
    books=relationship("Books",back_populates='user')
    categories=relationship("Categories",back_populates="user")

class Todo_items(Base):
    __tablename__ = 'todo_items'
    todo_uuid = Column(UUID(as_uuid=True),primary_key=True,index=True,unique=True,server_default=text("gen_random_uuid()"))
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("users.user_uuid"), index=True)
    todo_name = Column(String, index=True, nullable=False)
    todo_desc = Column(String, index=True)
    todo_urge = Column(String, index=True)
    todo_diff = Column(String, index=True)
    creation_date=Column(TIMESTAMP,nullable=False)
    due_date=Column(TIMESTAMP)
    user=relationship("Users",back_populates="todos")

class Books(Base):
    __tablename__ = 'books_items'
    book_uuid = Column(UUID(as_uuid=True),primary_key=True,index=True,unique=True,server_default=text("gen_random_uuid()"))
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("users.user_uuid"), index=True)
    book_name = Column(String, index=True, nullable=False)
    book_author = Column(String, index=True)
    book_desc = Column(String, index=True)
    user=relationship("Users",back_populates="books")


class Categories(Base):
    __tablename__ = "categories"
    cat_uuid = Column(UUID(as_uuid=True),primary_key=True,index=True,unique=True,server_default=text("gen_random_uuid()"))
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("users.user_uuid"), index=True)
    cat_name = Column(String, index=True, nullable=False)
    user=relationship("Users",back_populates="categories")
    items=relationship("Items",back_populates="category")

class Items(Base):
    __tablename__ = "items"
    item_uuid = Column(UUID(as_uuid=True),primary_key=True,index=True,unique=True,server_default=text("gen_random_uuid()"))
    cat_uuid = Column(UUID(as_uuid=True), ForeignKey("categories.cat_uuid"))
    item_name = Column(String, index=True, nullable=False)
    item_quantity = Column(Integer, index=True)
    item_price = Column(Integer, index=True)
    category=relationship("Categories",back_populates="items")



