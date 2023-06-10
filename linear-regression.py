import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=',')
x = data[:, 0]
y = data[:, 1]
x = x[0:int(len(x)*0.7)]
y = y[0:int(len(y)*0.7)]
test_data_x = x[int(len(x)*0.7):]
test_data_y = y[int(len(y)*0.7):]

w = 0
b = 0
lrate = 0.01
epochs = 1000

n = float(len(x))

for i in range(epochs):
    y_pred = w * x + b
    D_w = (2/n) * sum(x * (y_pred - y))
    D_b = (2/n) * sum(y_pred - y)
    w = w - lrate * D_w
    b = b - lrate * D_b

print(w, b)

y_pred = w * x + b

plt.scatter(x, y)
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color='red')
plt.show()

ys = 0
for i in range(len(test_data_x)):
    ys += abs(test_data_y[i] - (w * test_data_x[i] + b)) / test_data_y[i]

print((1-ys / len(test_data_x)) * 100)

plt.scatter(test_data_x, test_data_y)
plt.plot([min(test_data_x), max(test_data_x)], [min(y_pred), max(y_pred)], color='red')
plt.show()