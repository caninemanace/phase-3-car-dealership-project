from models.car import Car
from models.customer import Customer
from models.sale import Sale
from models.salesman import Salesman
from models.base import SessionLocal

CAR_MAKES = ["Toyota", "Honda", "Ford", "BMW", "Nissan"]
CAR_TYPES = ["Sedan", "SUV", "Truck", "Coupe", "Hatchback"]

COMMISSION_RATE = 0.05  

def add_car(session):
    print("\nAvailable Car Makes:")
    for idx, make in enumerate(CAR_MAKES, start=1):
        print(f"{idx}. {make}")

    try:
        make_index = int(input("Choose a car make by number: ")) - 1
        make = CAR_MAKES[make_index]
    except (IndexError, ValueError):
        print("Invalid make selection.")
        return

    model = input("Enter car model: ")

    print("\nAvailable Car Types:")
    for idx, car_type in enumerate(CAR_TYPES, start=1):
        print(f"{idx}. {car_type}")

    try:
        type_index = int(input("Choose a car type by number: ")) - 1
        car_type = CAR_TYPES[type_index]
    except (IndexError, ValueError):
        print("Invalid type selection.")
        return

    year = int(input("Enter car year: "))
    price = float(input("Enter car price: "))

    car = Car(make=make, model=model, year=year, price=price, car_type=car_type)
    session.add(car)
    session.commit()
    print(f"Car {make} {model} ({car_type}) added with ID {car.id}")


def add_customer(session):
    name = input("Enter customer name: ")
    phone = input("Enter phone number (optional): ")
    email = input("Enter email (optional): ")

    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()
    print(f"Customer {name} added with ID {customer.id}")


def add_salesman(session):
    name = input("Enter salesman's name: ")
    email = input("Enter email (optional): ")
    phone = input("Enter phone number (optional): ")

    salesman = Salesman(name=name, email=email, phone=phone)
    session.add(salesman)
    session.commit()
    print(f"Salesman {name} added with ID {salesman.id}")


def record_sale(session):
    car_id = int(input("Enter car ID to sell: "))
    customer_id = int(input("Enter customer ID: "))
    sale_price = float(input("Enter sale price: "))

    car = session.get(Car, car_id)
    customer = session.get(Customer, customer_id)

    if not car:
        print(f"No car found with ID {car_id}")
        return
    if not car.available:
        print(f"Car ID {car_id} is already sold.")
        return
    if not customer:
        print(f"No customer found with ID {customer_id}")
        return

    salesmen = session.query(Salesman).all()
    if not salesmen:
        print("No salesmen available. Please add a salesman first.")
        return

    print("\nAvailable Salesmen:")
    for s in salesmen:
        print(f"{s.id}. {s.name}")

    salesman_id = int(input("Enter salesman ID: "))
    salesman = session.get(Salesman, salesman_id)
    if not salesman:
        print(f"No salesman found with ID {salesman_id}")
        return

    if sale_price < car.price:
        confirm = input(f"Warning: Sale price (${sale_price:.2f}) is lower than original (${car.price:.2f}). Proceed? (y/n): ")
        if confirm.lower() != 'y':
            print("Sale cancelled.")
            return

    commission = (sale_price - car.price) * COMMISSION_RATE if sale_price > car.price else 0.0

    sale = Sale(
        car_id=car_id,
        customer_id=customer_id,
        sale_price=sale_price,
        salesman_id=salesman_id,
        commission=commission
    )
    car.available = False
    session.add(sale)
    session.commit()

    print(f"Sale recorded with ID {sale.id}. Car ID {car_id} sold by {salesman.name}.")
    print(f"Commission Earned: ${commission:.2f}")


def sales_report(session):
    sales = session.query(Sale).all()
    print("\n--- Sales Report ---")
    for sale in sales:
        car = session.get(Car, sale.car_id)
        salesman = session.get(Salesman, sale.salesman_id)
        if car:
            diff = sale.sale_price - car.price
            status = "Profit" if diff > 0 else "Loss" if diff < 0 else "Break-even"
            print(f"Sale ID: {sale.id} | Car: {car.make} {car.model} ({car.year})")
            print(f"  Sold by: {salesman.name if salesman else 'Unknown'}")
            print(f"  Original Price: ${car.price:.2f}")
            print(f"  Sale Price:     ${sale.sale_price:.2f}")
            print(f"  Result: {status} of ${abs(diff):.2f}")
            print(f"  Commission:     ${sale.commission:.2f}\n")


def salesman_commissions(session):
    print("\n--- Salesman Commissions Report ---")
    salesmen = session.query(Salesman).all()
    for s in salesmen:
        sales = session.query(Sale).filter_by(salesman_id=s.id).all()
        total_commission = sum(sale.commission or 0 for sale in sales)
        print(f"{s.name}: ${total_commission:.2f}")


def list_cars(session):
    cars = session.query(Car).all()
    print("\nAll Cars:")
    for car in cars:
        status = "Available" if car.available else "Sold"
        print(f"{car} - Status: {status}")


def list_customers(session):
    customers = session.query(Customer).all()
    print("\nAll Customers:")
    for customer in customers:
        print(customer)


def list_sales(session):
    sales = session.query(Sale).all()
    print("\nAll Sales:")
    for sale in sales:
        print(sale)


def menu():
    session = SessionLocal()

    while True:
        print("\n--- Car Dealership Menu ---")
        print("1. Add Car")
        print("2. Add Customer")
        print("3. Add Salesman")
        print("4. Record Sale")
        print("5. List Cars")
        print("6. List Customers")
        print("7. List Sales")
        print("8. Sales Report")
        print("9. Salesman Commissions")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_car(session)
        elif choice == "2":
            add_customer(session)
        elif choice == "3":
            add_salesman(session)
        elif choice == "4":
            record_sale(session)
        elif choice == "5":
            list_cars(session)
        elif choice == "6":
            list_customers(session)
        elif choice == "7":
            list_sales(session)
        elif choice == "8":
            sales_report(session)
        elif choice == "9":
            salesman_commissions(session)
        elif choice == "10":
            print("Shutting down the application.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

    session.close()


if __name__ == "__main__":
    menu()

