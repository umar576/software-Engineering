import math

def quadratic_weather_model_multiple():
    try:
        with open("weather_coefficients_multiple.txt", "r") as file:
            for line in file:
                try:
                    a, b, c = map(float, line.split())
                except ValueError:
                    print("Skipping invalid line:", line.strip())
                    continue

                delta = b**2 - 4 * a * c

                if delta > 0:
                    root1 = (-b + math.sqrt(delta)) / (2 * a)
                    root2 = (-b - math.sqrt(delta)) / (2 * a)
                    print(f"Multiple Inputs: Roots {root1:.2f} and {root2:.2f}")
                elif delta == 0:
                    root = -b / (2 * a)
                    print(f"Multiple Inputs: Single root {root:.2f}")
                else:
                    print("Multiple Inputs: No real solutions for coefficients:", a, b, c)
    except FileNotFoundError:
        print("Error: File not found.")

quadratic_weather_model_multiple()