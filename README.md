## Team
This project was developed by:

María Noriega

Carlos Castro

# Customer Order Management System

## Project Description
This project is a terminal-based Customer Order Management System developed in Python.  
The system allows the user to register clients, register products, create orders, consult registered orders, calculate daily income, and generate a final sales report.

The solution was built using **dictionaries** and **tuples** as the main data structures, following the challenge requirements.  
It also uses functions to organize the logic of the program, making the code more modular, clear, and reusable.

---

## System Architecture
The program follows a modular structure based on functions.  
Each function has a specific responsibility inside the system.

### Main components:
- **System data container**: stores clients, products, orders, and the order counter.
- **Validation functions**: verify that text fields are not empty and that numeric values are valid and positive.
- **Registration functions**: register clients and products in the system.
- **Order management functions**: create orders and calculate order totals.
- **Reporting functions**: consult orders, calculate daily income, group orders by client, summarize sold products, and generate the final report.
- **Menu functions**: display the menu, process user options, and run the system loop.

---

## Instructions to Run the Program
1. Make sure Python 3 is installed on your computer.
2. Save the file as `sistema_pedidos_completo_espanol.py` or any preferred name.
3. Open a terminal in the folder where the file is located.
4. Run the program with the following command:

```bash
python sistema_pedidos_completo_espanol.py
```

5. Use the menu options displayed in the terminal:
- Register client
- Register product
- Create order
- Consult orders
- Calculate daily income
- Generate final report
- Exit

---

## Data Structures Used

### 1. Dictionaries
Dictionaries are used to store:
- **Clients**
- **Products**
- **Orders**
- **Grouped report data**

They allow fast access to data through unique keys such as client ID, product ID, or order ID.

### 2. Tuples
Tuples are used to store product information:
- Product ID
- Product name
- Unit price

A tuple is appropriate here because product data is grouped in a fixed structure.

### 3. Strings
Strings are used for:
- Names
- Emails
- IDs
- Messages
- Reports

### 4. Integers and Floats
- **Integers** are used for counters and quantities.
- **Floats** are used for prices, totals, and income calculations.

---

## Description of the Implemented Modules

### 1. Data Creation Module
This part creates the main structure of the system:
- `crear_datos_sistema()`

### 2. Validation Module
This module validates user input:
- `validar_texto_no_vacio()`
- `validar_flotante_positivo()`
- `validar_entero_positivo()`

### 3. Client Module
This module registers clients:
- `registrar_cliente()`

### 4. Product Module
This module registers products:
- `registrar_producto()`

### 5. Order Module
This module creates and manages orders:
- `calcular_total_pedido()`
- `crear_pedido()`

### 6. Query and Reporting Module
This module generates information and reports:
- `formatear_catalogo_clientes()`
- `formatear_catalogo_productos()`
- `consultar_pedidos()`
- `calcular_ingresos_diarios()`
- `agrupar_pedidos_por_cliente()`
- `resumir_productos_vendidos()`
- `generar_reporte_final()`

### 7. Menu Module
This module controls interaction with the user:
- `construir_texto_menu()`
- `procesar_opcion_menu()`
- `ejecutar_sistema()`

---

## Conclusion
This project demonstrates how to build a functional order management system using Python fundamentals.  
It applies modular programming, validation, structured data storage, and report generation in a console-based application.
