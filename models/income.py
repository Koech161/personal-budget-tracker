from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Income(Base):
    __tablename__ = 'incomes'    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship('User', back_populates='incomes')

    def __repr__(self):
        return f'Income(id={self.id}, source={self.source}, amount={self.amount}, date={self.date})'
