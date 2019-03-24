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


def to_complex(signal):
    return [(x, 0) for x in signal]


def mult_complex(first, second):
    return ((first[0] * second[0]) - (first[1] * second[1]), (first[0] * second[1]) + (first[1] * second[0]))


def sum_complex(first, second):
    return (first[0] + second[0], first[1] + second[1])


def sub_complex(first, second):
    return (first[0] - second[0], first[1] - second[1])


def from_polar(r, radians):
    return ((r * math.cos(radians)), (r * math.sin(radians)))


def magnitude(complex):
    return math.sqrt(math.pow(complex[0], 2) + math.pow(complex[1], 2))


def phase(complex):
    return math.atan(complex[1] / complex[0])


def fdft(signal):
    N = len(signal)
    e = list()
    d = list()
    X = [None] * N

    if N == 1:
        return [signal[0]]

    for k in range(0, int(N / 2)):
        e.append(signal[2 * k])
        d.append(signal[2 * k + 1])

    D = fdft(d)
    E = fdft(e)

    for k in range(0, int(N / 2)):
        tmp = from_polar(1, -2 * math.pi * k / N)
        D[k] = mult_complex(D[k], tmp)

    for k in range(0, int(N / 2)):
        X[k] = sum_complex(E[k], D[k])
        X[k + int(N / 2)] = sub_complex(E[k], D[k])

    return X


x = to_complex(generate_full_signal(n, N, w))
transformed = [magnitude(complex) for complex in fdft(x)]

x_axis = range(0, N)

fig = plt.figure()

x_plot = fig.add_subplot(2, 1, 1)
x_plot.grid(True)
x_plot.plot(x_axis, x)

y_plot = fig.add_subplot(2, 1, 2)
y_plot.grid(True)
y_plot.plot(x_axis, transformed)

plt.show()
