import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # нижня межа
b = 2  # верхня межа


# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)
    mean_value = np.mean(func(x_random))
    area = (b - a) * mean_value
    return area


monte_carlo_result = monte_carlo_integration(f, a, b)


# Перевіряємо результат за допомогою методу quad
quad_result, quad_error = spi.quad(f, a, b)


print(f"Результат методу Монте-Карло: {monte_carlo_result}")
print(f"Результат методу quad: {quad_result}")
print(f"Похибка методу quad: {quad_error}")

# Створення діапазону значень для x
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Інтегрування f(x) = x^2 від {a} до {b}')

plt.grid()
plt.show()
