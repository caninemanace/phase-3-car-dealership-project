from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    salesman_id = Column(Integer, ForeignKey("salesmen.id"))
    sale_price = Column(Float, nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow)
    commission = Column(Float, nullable=True)

    car = relationship("Car")
    customer = relationship("Customer")
    salesman = relationship('Salesman') 

    def __repr__(self):
        return (f"<Sale(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, "
                f"sale_price={self.sale_price}, sale_date={self.sale_date})>")
