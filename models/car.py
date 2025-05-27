from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Car(id={self.id}, make='{self.make}', model='{self.model}', year={self.year}, price={self.price})>"
