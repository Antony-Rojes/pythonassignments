from std.calculator import add, subtract, multiply, divide
from high.scientific_calculator import (square_root, power, logarithm, sine, cosine, tangent,
    factorial, exponential, degrees_to_radians,
    radians_to_degrees)

operation=input("Enter The Calculator Type (Standard or Scientific) : ")
if operation.lower()=='standard':
    a = int(input("Enter Number 1 for performing (Addition/Subraction/Multiplication/Division) : "))
    b = int(input("Enter Number 2 for performing (Addition/Subraction/Multiplication/Division) : "))
    print(f"Addition : {add(a, b)}")
    print(f"Subtraction : {subtract(a, b)}")
    print(f"Multiplication : {multiply(a, b)}")
    print(f"Division : {divide(a, b)}")

elif operation.lower()=='scientific':
    angle = int(input("Enter an angle (in degrees) : "))
    print(f"Sine({angle}°) : {sine(angle)}") 
    print(f"Cosine({angle}°) : {cosine(angle)}")
    print(f"Tangent({angle}°) : {tangent(angle)}")
    a=int(input("Input for Squareroot : "))
    print(f"Square Root of {a} : {square_root(a)}")
    a=int(input("Enter base (a) : "))
    b=int(input("Enter exponent (b) : "))
    print(f"{a} raised to power {b} : {power(a, b)}")
    a=int(input("Input (a) for Log (base 10) : "))
    print(f"Logarithm of {a} (base 10) : {logarithm(a)}")
    a=int(input("Input (a) for Factorial : "))
    print(f"Factorial of {a} : {factorial(a)}")
    a=int(input("Input (a) for Exponential : "))
    print(f"Exponential of {a} (e^{a}) : {exponential(a)}")
    angle=int(input("Input (a) for Output Radian in Degrees : "))
    print(f"{angle} degrees in radians : {degrees_to_radians(angle)}")
    a=float(input("Input (a) for Output Degree in radians : "))
    print(f"{a} radians in degrees: {radians_to_degrees(a)}")
else:
    print("Invalid Operation!")    


