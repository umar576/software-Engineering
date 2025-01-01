import math

def quadratic_weather_model_input():
    print("Enter coefficients for the quadratic equation (ax^2 + bx + c):")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    delta = b**2 - 4 * a * c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Keyboard Input: Weather factors have roots {root1:.2f} and {root2:.2f}")
    elif delta == 0:
        root = -b / (2 * a)
        print(f"Keyboard Input: Weather factors have a single root {root:.2f}")
    else:
        print("Keyboard Input: Weather conditions lead to no real solutions.")

quadratic_weather_model_input()
