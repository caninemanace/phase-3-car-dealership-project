from models.base import Base, engine
from models.car import Car
from models.customer import Customer   
from models.sale import Sale            

def setup_database():
    Base.metadata.create_all(engine)
    print("Database and tables created!")

if __name__ == "__main__":
    setup_database()

