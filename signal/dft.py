import matplotlib.pyplot as plt
import math
import random
from datetime import datetime

n = 12
N = 64
w = 1100


def create_signal(n, w):
	A = random.uniform(0, 2) + 2
	phi = random.uniform(0, 2 * math.pi)
	return [(A * math.sin(w * x + phi)) for x in range(0, n)]


def Mx(harmonic):
	return sum(harmonic) / len(harmonic)


def create_harmonics(n, N, w):
	return [(create_signal(N, w * (x + 1) / n)) for x in range(0, n)]


def combine(harmonics):
	combined = []
	for j in range(len(harmonics[0])):
		sum = 0
		for i in range(len(harmonics)):
			sum += harmonics[i][j]
		combined.append(sum)
	return combined


def generate_full_signal(n, N, w):
    harmonics = create_harmonics(n, N, w)
    return combine(harmonics)


def dft(x):
    res = list()
    for p in range(0, N):
        real = 0
        imaginary = 0
        for k in range(0, N):
            tmp = 2 * math.pi * p * k / N
            real += x[k] * math.cos(tmp)
            imaginary += x[k] * math.sin(tmp)
        res.append(math.sqrt(math.pow(real, 2) + math.pow(imaginary, 2)))
    return res


x = generate_full_signal(n, N, w)
transformed = dft(x)

x_axis = range(0, N)

fig = plt.figure()

x_plot = fig.add_subplot(2, 1, 1)
x_plot.grid(True)
x_plot.plot(x_axis, x)

y_plot = fig.add_subplot(2, 1, 2)
y_plot.grid(True)
y_plot.plot(x_axis, transformed)

plt.show()