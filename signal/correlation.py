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


def correlation(x, y, tau):
	mx = Mx(x)
	my = Mx(y)
	return sum([correlation_partial(x[i], mx, y[i + tau], my) for i in range(0, len(x))]) / (len(x) - 1)


def Rxy(x, y):
	return [(correlation(x[:int(N / 2)], y, tau)) for tau in range(0, int(N / 2))]


def correlation_partial(xi, mx, yi, my):
    return (xi - mx) * (yi - my)


start = datetime.now().microsecond / 1000.0

x = generate_full_signal(n, N, w)

y = generate_full_signal(n, N, w)

rxx = Rxy(x, x)
ryy = Rxy(y, y)
rxy = Rxy(x, y)

end = datetime.now().microsecond / 1000.0

print("T = " + str(end - start) + "ms")

x_axis = range(0, int(N/2))

# plt.plot(x_axis, rxx)
# plt.show()
#
# plt.plot(x_axis, ryy)
# plt.show()
#
# plt.plot(x_axis, rxy)
# plt.show()

fig = plt.figure()

x_plot = fig.add_subplot(3, 1, 1)
x_plot.grid(True)
x_plot.plot(x_axis, rxx)

y_plot = fig.add_subplot(3, 1, 2)
y_plot.grid(True)
y_plot.plot(x_axis, ryy)

xy_plot = fig.add_subplot(3, 1, 3)
xy_plot.grid(True)
xy_plot.plot(x_axis, rxy)

plt.show()