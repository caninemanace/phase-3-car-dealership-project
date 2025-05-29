# phase-3-car-dealership-project

This is a Python-based CLI (Command-Line Interface) application for managing a car dealership. The app allows you to add and manage cars, customers, salesmen, and record car sales with commissions using a SQLite database via SQLAlchemy ORM.

---

## Features

- Add, update, and delete cars, customers, and salesmen
- Record a car sale and automatically calculate commission
- View detailed sales reports and commissions by salesman
- List all cars, customers, and sales
- Track sold vs. available cars

---

## Project Structure

```
car_dealership/
├── app.py                  # CLI logic (entry point)
├── models/
│   ├── __init__.py
│   ├── base.py             # Base declarative setup
│   ├── car.py              # Car model
│   ├── customer.py         # Customer model
│   └── sale.py             # Sale model
├── db/
│   └── setup.py            # Create tables and seed data
├── cli/
│   └── menu.py             # CLI menu system
├── requirements.txt
└── README.md
```

- **app.py**: Main entry point for the CLI application.
- **models/**: Contains SQLAlchemy ORM models and base setup.
- **db/setup.py**: Handles database table creation and seeding.
- **cli/menu.py**: Implements the CLI menu and user interaction.
- **requirements.txt**: Lists Python dependencies.
- **README.md**: Project documentation.

---

## Example Use Cases

- Add a new car and list all available cars
- Add customers and salesmen
- Record a sale with automatic commission
- View a full sales report or see each salesman’s earnings

---

## Future Improvements

- Add search and filter functionality
- Export reports to CSV or PDF
- Add authentication for salesmen
- Build a GUI or web interface

---

## 🛠️ Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/caninemanace/phase-3-car-dealership-project.git
    cd phase-3-car-dealership-project
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database (if required)**
    ```bash
    python db/setup.py
    ```

---

## Running the App

To launch the CLI menu, run:

```bash
python -m cli.menu
```

---

## Dependencies

See `requirements.txt` for the full list. Main dependencies include:

- SQLAlchemy
- tabulate
- colorama

---

## License

This project is licensed under the MIT License.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Contact

For questions or suggestions, open an issue on [GitHub](https://github.com/caninemanace/phase-3-car-dealership-project).
