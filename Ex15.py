import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def logarithm(a):
    return math.log10(a)

# Calling the functions

print("\n*********Scientific Calculator**********")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
angle = float(input("Enter angle: "))

print("\n********************************")
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Power:", power(a, b))
print("Square Root:", square_root(a))
print("Sine:", sine(angle))
print("Cosine:", cosine(angle))
print("Tangent:", tangent(angle))
print("Logarithm:", logarithm(a))
