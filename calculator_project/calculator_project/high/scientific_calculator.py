import math

def square_root(a):
    """Returns the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def power(a, b):
    """Returns a raised to the power of b (a^b)."""
    return math.pow(a, b)

def logarithm(a, base=10):
    """Returns the logarithm of a number with a given base."""
    if a <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log(a, base)

def sine(angle):
    """Returns the sine of an angle (in degrees)."""
    return math.sin(math.radians(angle))

def cosine(angle):
    """Returns the cosine of an angle (in degrees)."""
    return math.cos(math.radians(angle))

def tangent(angle):
    """Returns the tangent of an angle (in degrees)."""
    return math.tan(math.radians(angle))

def factorial(n):
    """Returns the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def exponential(x):
    """Returns the exponential of x (e^x)."""
    return math.exp(x)

def natural_log(a):
    """Returns the natural logarithm (base e) of a number."""
    if a <= 0:
        raise ValueError("Natural logarithm is not defined for non-positive numbers")
    return math.log(a)

def degrees_to_radians(deg):
    """Converts degrees to radians."""
    return math.radians(deg)

def radians_to_degrees(rad):
    """Converts radians to degrees."""
    return math.degrees(rad)

def arcsine(value):
    """Returns the arcsine (in degrees) of a value."""
    if value < -1 or value > 1:
        raise ValueError("Input should be between -1 and 1 for arcsine")
    return math.degrees(math.asin(value))

def arccosine(value):
    """Returns the arccosine (in degrees) of a value."""
    if value < -1 or value > 1:
        raise ValueError("Input should be between -1 and 1 for arccosine")
    return math.degrees(math.acos(value))

def arctangent(value):
    """Returns the arctangent (in degrees) of a value."""
    return math.degrees(math.atan(value))

if __name__ == "__main__":
    angle = int(input("Enter an angle (in degrees): "))
    print(f"Sine({angle}°):", sine(angle))
    print(f"Cosine({angle}°):", cosine(angle))
    print(f"Tangent({angle}°):", tangent(angle))
    print(f"Square Root of 16:", square_root(16))
    print(f"2 raised to power 3:", power(2, 3))
    print(f"Logarithm of 100 (base 10):", logarithm(100))
    print(f"Factorial of 5:", factorial(5))
    print(f"Exponential of 2 (e^2):", exponential(2))
    print(f"Natural Logarithm of e:", natural_log(math.e))
    print(f"Degrees to Radians (180°):", degrees_to_radians(180))
    print(f"Radians to Degrees (π):", radians_to_degrees(math.pi))
    print(f"Arcsine(0.5):", arcsine(0.5))
    print(f"Arccosine(0.5):", arccosine(0.5))
    print(f"Arctangent(1):", arctangent(1))
