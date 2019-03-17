import matplotlib.pyplot as plt
import math
import random

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


def Rxy(x, mx, y, my, number):
    return sum(
        [correlation_partial(x[i], mx, y[i], my) for i in range(0, number)]
    ) / (number - 1)


def Rxx(x, mx, shift, number):
    return sum(
        [correlation_partial(x[i], mx, x[i + shift], mx) for i in range(0, number - shift)]
    ) / (number - shift - 1)


def correlation_partial(xi, mx, yi, my):
    return (xi - mx) * (yi - my)


x = generate_full_signal(n, N, w)
mx = Mx(x)
rxx = Rxx(x, mx, 1, N)

y = generate_full_signal(n, N, w)
my = Mx(y)

rxy = Rxy(x, mx, y, my, N)

print("Rxx = " + str(rxx))
print("Rxy = " + str(rxy))

x_axis = range(0, N)
fig = plt.figure()

x_plot = fig.add_subplot(2, 1, 1)
x_plot.grid(True)
x_plot.plot(x_axis, x)

y_plot = fig.add_subplot(2, 1, 2)
y_plot.grid(True)
y_plot.plot(x_axis, y)

plt.show()