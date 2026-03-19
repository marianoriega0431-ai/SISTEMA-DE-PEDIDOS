# Customer Order Management System

## Project Description
This project is a simple **Customer Order Management System** developed in Python.

The program allows the user to:
- register clients
- register products
- create orders
- view registered orders
- calculate daily income
- generate a final report

This system was created to organize customer orders in a structured way and make sales management easier during the working day.

## Problem Context
In many small businesses, orders are often recorded manually. This can cause problems such as:
- lack of control over registered clients
- difficulty identifying sold products
- manual calculation errors
- no clear daily sales summary

This program solves that problem by storing the information in dictionaries and tuples and calculating totals automatically.

## Main Features

### 1. Register Clients
The system allows the user to save client information:
- client ID
- client name
- client email

### 2. Register Products
The system allows the user to save product information using tuples:
- product ID
- product name
- unit price

### 3. Create Orders
The user can create an order by linking:
- a client
- a product
- a quantity

The system calculates the total automatically:

`total = unit_price * quantity`

### 4. View Orders
The program displays all registered orders with:
- order ID
- client name
- product name
- quantity
- total

### 5. Calculate Daily Income
The system adds the total value of all orders and shows the daily income.

### 6. Generate Final Report
The final report includes:
- total number of orders
- total income
- orders grouped by client
- products sold during the day

## Data Structures Used

### Dictionary
Dictionaries were used to store:
- clients
- products
- orders

They make it easier to access information using an ID as a key.

### Tuple
Tuples were used to represent products because product data should remain structured and fixed.

Example:
```python
(product_id, product_name, unit_price)
