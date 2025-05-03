from std.calculator import add, subtract, multiply, divide
from high.scientific_calculator import (
    square_root, power, logarithm, sine, cosine, tangent,
    factorial, exponential, natural_log, degrees_to_radians,
    radians_to_degrees, arcsine, arccosine, arctangent
)

a = int(input("Enter input for a: "))
b = int(input("Enter input for b: "))

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")

angle = int(input("Enter an angle (in degrees): "))
print(f"Sine({angle}°): {sine(angle)}")
print(f"Cosine({angle}°): {cosine(angle)}")
print(f"Tangent({angle}°): {tangent(angle)}")

print(f"Square Root of {a}: {square_root(a)}")
print(f"{a} raised to power {b}: {power(a, b)}")
print(f"Logarithm of {a} (base 10): {logarithm(a)}")


print(f"Factorial of {a}: {factorial(a)}")
print(f"Exponential of {a} (e^{a}): {exponential(a)}")
print(f"Natural Logarithm of {a}: {natural_log(a)}")
print(f"{angle} degrees in radians: {degrees_to_radians(angle)}")
print(f"{a} radians in degrees: {radians_to_degrees(a)}")

val = float(input("Enter a value between -1 and 1 for inverse trig: "))
print(f"Arcsine({val}): {arcsine(val)}°")
print(f"Arccosine({val}): {arccosine(val)}°")
print(f"Arctangent({val}): {arctangent(val)}°")
