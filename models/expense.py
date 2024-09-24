from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)

    user = relationship('User', back_populates='expenses') 
    category = relationship('Category', back_populates='expenses') 

    def __repr__(self):
        return f'Expense(id={self.id}, amount={self.amount}, date={self.date}, description={self.description})'
