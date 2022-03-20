from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"