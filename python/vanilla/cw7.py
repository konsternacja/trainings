import random
import math
import matplotlib.pyplot as plt
import numpy as np

# cw1
def get_random_sequence(length):
    base_pairs = ["A", "T", "G", "C"]
    return ''.join(random.choices(base_pairs, k=length))


print(get_random_sequence(10))

# cw2
def f(x):
    # równanie 2*x**2 - 5*x + 3 = 0 
    return 2*x**2 - 5*x + 3

def df(x):
    # pochodna 4*x - 5
    return 4*x - 5

x = 0 # zgadujemy

for i in range(1, 101):
    new_x = x - f(x)/df(x)
    
    if abs(new_x - x) < 0.000001:
        break
        
    x = new_x
    
print(f"Miejsce zerowe w x = {new_x:.2f} znalezione w {i} iteracjach")


# cw3
class LinearRegression:
    def __init__(self):
        self.a = 0
        self.b = 0

    def fit(self, x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        mean_x = sum_x / n
        mean_y = sum(y) / n
        sum_xy = sum([xi*yi for xi, yi in zip(x, y)])
        sum_xx = sum([xi**2 for xi in x])

        self.b = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)
        self.a = (sum_y - self.b*sum_x) / n

    def predict(self, x):
        return [self.a + self.b*xi for xi in x]

    def calc_r_squared(self, x, y):
        y_pred = self.predict(x)
        ssr = sum([(yi - y_predi)**2 for yi, y_predi in zip(y, y_pred)])
        mean_y = sum(y) / len(y)
        sst = sum([(yi - mean_y)**2 for yi in y])
        return 1 - (ssr/sst)
        
        
model = LinearRegression()

# synthetic data
def generate_synthetic_data(a, b, x_range, size, noise):
    x = [random.uniform(x_range[0], x_range[1]) for _ in range(size)]
    y = [a * xi + b + random.gauss(0, noise) for xi in x]
    return x, y

# Fit the model 
x, y = generate_synthetic_data(2, 1, (0, 10), 100, 0.5)
model.fit(x, y)


# Predictions
x_new = [1.5, 2.5, 3.5, 4.5, 6]
predictions = model.predict(x_new)
print(f"Predictions: {predictions}")

# R-squared
r_squared = model.calc_r_squared(x, y)
print(f"R-squared: {r_squared}")

# Generate a range of x values
x_values = [min(x) + i*(max(x) - min(x))/100 for i in range(101)]

# Calculate the corresponding y values
y_values = model.predict(x_values)

# Plot the original data points
plt.scatter(x, y)

# Plot the line
plt.plot(x_values, y_values, color='red')

plt.show()

