from sqlalchemy import Column, Integer, String
from models.base import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', phone='{self.phone}', email='{self.email}')>"
