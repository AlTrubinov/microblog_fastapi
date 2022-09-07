from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = 'microblog posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(length=350))
    data = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')
