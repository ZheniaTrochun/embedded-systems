import matplotlib.pyplot as plt
import math
import random
from datetime import datetime

n = 12
N = 64
w = 1100


def create_signal(n, w, xarr):
	A = random.uniform(0, 2) + 2
	phi = random.uniform(0, 2 * math.pi)
	return [(A * math.sin(w * x + phi)) for x in xarr]


def Mx(harmonic):
	return sum(harmonic) / len(harmonic)


def Dx(harmonic, mx):
	partial_results = [((x - mx) ** 2) for x in harmonic]
	return sum(partial_results) / (len(harmonic) - 1)


def create_harmonics(n, N, w, xarr):
	return [(create_signal(N, w * (x + 1) / n, xarr)) for x in range(0, n)]


def combine(harmonics):
	combined = []
	for j in range(len(harmonics[0])):
		sum = 0
		for i in range(len(harmonics)):
			sum += harmonics[i][j]
		combined.append(sum)
	return combined


def draw_harmonics(x, harmonics, fig):
	axn = fig.add_subplot(2, 1, 1)
	axn.grid(True)
	for ind, harmonic in enumerate(harmonics):
		axn.plot(x, harmonic)


def draw_combined(x, combined, fig):
	combined_plot = fig.add_subplot(2, 1, 2)
	combined_plot.grid(True)
	combined_plot.plot(x, combined)


step = 1 / float(N)

x = [(x * step) for x in range(0, N)]

start = datetime.now().microsecond / 1000.0

harmonics = create_harmonics(n, N, w, x)
combined = combine(harmonics)

# m = [Mx(x) for x in harmonics]
# d = [Dx(x, m[ind]) for ind, x in enumerate(harmonics)]

mx = Mx(combined)
dx = Dx(combined, mx)

end = datetime.now().microsecond / 1000.0

fig = plt.figure()

draw_harmonics(x, harmonics, fig)
draw_combined(x, combined, fig)

print("Mx = " + str(mx))
print("Dx = " + str(dx))
print("T = " + str(end - start) + "ms")

plt.show()