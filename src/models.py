from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index =True)
    username = Column(String(50), unique = True)
    hashed_password = Column(String(100))

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    post = Column(String (100))
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates = "posts")
