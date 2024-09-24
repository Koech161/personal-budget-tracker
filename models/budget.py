from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id')) 
    amount = Column(Float, nullable=False) 
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)

    category = relationship('Category', back_populates='budgets')

    def __repr__(self):
        return f'Budget(id={self.id}, amount={self.amount}, period_start={self.period_start}, period_end={self.period_end})'
