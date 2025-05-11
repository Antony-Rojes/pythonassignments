import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)
def power(a, b):
    return math.pow(a, b)
def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log(a, base)
def sine(angle):
    return math.sin(math.radians(angle))
def cosine(angle):
    return math.cos(math.radians(angle))
def tangent(angle):
    return math.tan(math.radians(angle))
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)
def exponential(x):
    return math.exp(x)
def degrees_to_radians(deg):
    return math.radians(deg)
def radians_to_degrees(rad):
    return math.degrees(rad)
if __name__ == "__main__":
        print("----Scientific Calculator----")
    