import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 3 + 3

# Межі інтегрування
a = 0
b = 3

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(f, a, b, num_points):
    x_random = np.random.uniform(a, b, num_points)
    y_random = f(x_random)
    integral_estimate = (b - a) * np.mean(y_random)
    return integral_estimate

# Кількість випадкових точок
num_points = 100000

# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b, num_points)
print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")

# Обчислення інтегралу за допомогою SciPy quad
quad_result, quad_error = spi.quad(f, a, b)
print(f"Інтеграл за допомогою quad: {quad_result}, з помилкою: {quad_error}")

# Візуалізація функції та області інтегрування
x = np.linspace(-0.5, 3.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'g', linewidth=3)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='blue', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^3 + 3 від 0 до 3')
plt.grid()
plt.show()
