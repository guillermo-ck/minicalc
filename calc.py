C:\Users\guill\Programitas\sda\minicalc# calc.py
# calc.py
import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    logging.info(f"Subtracting {a} - {b}")
    return a - b

def power(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
