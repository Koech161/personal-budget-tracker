from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    expenses = relationship('Expense', back_populates='category')
    budgets = relationship('Budget', back_populates='category')
    user = relationship('User', back_populates='categories')

    def __repr__(self):
        return f'Category(id={self.id}, name={self.name})'
