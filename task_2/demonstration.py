import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2
f_max = f(b)
N = 5000  # Менше точок для кращої візуалізації

# Метод 1: Середнє значення функції
x1 = np.random.uniform(a, b, N)
y1 = f(x1)
monte_carlo_1 = (b - a) * np.mean(y1)

# Метод 2: Підрахунок попадань
x2 = np.random.uniform(a, b, N)
y2 = np.random.uniform(0, f_max, N)
under_curve = y2 <= f(x2)
monte_carlo_2 = (b - a) * f_max * np.sum(under_curve) / N

# Точний інтеграл
quad_result, _ = quad(f, a, b)

# Побудова графіка
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(12, 6))

# Графік функції
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x²')
ax.fill_between(x, y, where=(x >= a) & (x <= b), color='gray', alpha=0.3, label='Площа під кривою')

# Точки методу 1 (лише f(x_i), сині)
ax.scatter(x1, y1, s=10, color='blue', alpha=0.3, label='Метод 1: f(x_i)')

# Точки методу 2: під та над кривою
ax.scatter(x2[under_curve], y2[under_curve], s=10, color='green', alpha=0.4, label='Метод 2: під кривою')
ax.scatter(x2[~under_curve], y2[~under_curve], s=10, color='orange', alpha=0.4, label='Метод 2: над кривою')

# Оформлення
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, f_max + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Інтегрування f(x) = x² методом Монте-Карло\nМетод 1 (середнє значення на кривій): {monte_carlo_1:.5f} | Метод 2 (попадання під криву): {monte_carlo_2:.5f} | Quad: {quad_result:.5f}')
ax.legend()
plt.grid()
plt.show()