import math

def quadratic_weather_model():
    a, b, c = 1.0, -3.0, 2.0

    delta = b**2 - 4 * a * c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Hardcoded Variables: Weather factors have roots {root1:.2f} and {root2:.2f}")
    elif delta == 0:
        root = -b / (2 * a)
        print(f"Hardcoded Variables: Weather factors have a single root {root:.2f}")
    else:
        print("Hardcoded Variables: Weather conditions lead to no real solutions.")

quadratic_weather_model()