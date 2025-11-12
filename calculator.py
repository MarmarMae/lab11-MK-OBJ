# https://github.com/MarmarMae/lab11-MK-OBJ
# Partner 1: Marley Kight
# Partner 2:
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print("Error calculating hypotenuse:", e)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm base and argument must be positive, and base cannot be 1.")
    return math.log(a, b)

def exp(a, b):
    return a ** b
