from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    incomes = relationship('Income', back_populates='user')
    expenses = relationship('Expense', back_populates='user')
    categories = relationship('Category', back_populates='user')

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, email={self.email})'
