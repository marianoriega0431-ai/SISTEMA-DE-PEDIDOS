Sistema de pedidos

Description

This project is a simple customer order management system developed in Python.

It was created as part of my learning process at Riwi, where I am currently starting to learn programming.

The system allows managing basic information about clients, products, and orders in an organized way.

Team

This project was developed by:

- María Noriega
- Carlos Castro

What the program does

The program allows the user to:

- Register clients (ID, name, email)
- Register products (ID, name, price)
- Create orders by selecting a client and a product
- Show all registered orders
- Calculate total income of the day
- Generate a final report

How it works

The system uses:

- Dictionaries to store clients, products, and orders
- Tuples to represent products (id, name, price)

Each order is created by linking a client with a product and a quantity.

The total of each order is calculated automatically:

total = unit_price * quantity

Challenges

One of the most challenging parts for me was calculating the total of each order and understanding how to connect the product price with the quantity.

This helped me better understand how to work with dictionaries and how to access data inside them.

How to run the program

1. Open the terminal
2. Make sure Python is installed
3. Run the file:

python nombre_del_archivo.py

4. Use the menu options to interact with the system

Final note

This project was made for learning purposes and helped me practice basic concepts such as functions, dictionaries, and program structure.
