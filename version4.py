import math
import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    roots = []

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        roots = [root1, root2]
        print(f"Two roots: {root1:.2f}, {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        roots = [root]
        print(f"One root: {root:.2f}")
    else:
        print("No real roots exist.")
    
    x = np.linspace(-10, 10, 500)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
    
    if roots:
        for root in roots:
            plt.scatter(root, 0, color='red', label=f'Root: {root:.2f}')
            plt.text(root, 0.5, f'({root:.2f}, 0)', color='red', fontsize=10)
    
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    plt.title(f"Graph of {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

a = 2
b = 5
c = -3

plot_quadratic(a, b, c)