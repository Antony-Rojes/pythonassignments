from std.calculator import add, subtract, multiply, divide
from std.scientific_calculator import square_root, power, logarithm, sine, cosine, tangent
a, b = 10, 5
print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
angle = 45
print(f"Sine({angle}°): {sine(angle)}")
print(f"Cosine({angle}°): {cosine(angle)}")
print(f"Tangent({angle}°): {tangent(angle)}")
print(f"Square Root of {a}: {square_root(a)}")
print(f"{a} raised to power {b}: {power(a, b)}")
print(f"Logarithm of {a} (base 10): {logarithm(a)}")
