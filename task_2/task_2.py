import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2
f_max = f(b)
N = 100000  # Кількість точок

#Метод 1: Монте-Карло через середнє значення функції
x_random_1 = np.random.uniform(a, b, N)
y_random_1 = f(x_random_1)
monte_carlo_1 = (b - a) * np.mean(y_random_1)

# --- Метод 2: Монте-Карло через підрахунок попадань під криву ---
x_random_2 = np.random.uniform(a, b, N)
y_random_2 = np.random.uniform(0, f_max, N)
under_curve = y_random_2 <= f(x_random_2)
monte_carlo_2 = (b - a) * f_max * np.sum(under_curve) / N

# --- Точне значення інтеграла (quad) ---
quad_result, quad_error = quad(f, a, b)

# --- Вивід результатів ---
print("Інтеграл методом Монте-Карло (середнє значення):", monte_carlo_1)
print("Інтеграл методом Монте-Карло (підрахунок попадань):", monte_carlo_2)
print("Інтеграл методом quad (еталонне значення):", quad_result)
print("Похибка методу 1:", abs(monte_carlo_1 - quad_result))
print("Похибка методу 2:", abs(monte_carlo_2 - quad_result))


#Побудова графіка з точками
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()
