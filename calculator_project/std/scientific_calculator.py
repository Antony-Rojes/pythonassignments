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

if __name__ == "__main__":
    angle = 30
    print(f"Sine({angle}°):", sine(angle))
    print(f"Cosine({angle}°):", cosine(angle))
    print(f"Tangent({angle}°):", tangent(angle))
    print(f"Square Root of 16:", square_root(16))
    print(f"2 raised to power 3:", power(2, 3))
    print(f"Logarithm of 100 (base 10):", logarithm(100))
