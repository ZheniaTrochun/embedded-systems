
sigma = 0.1

x1 = (1, 5)
x2 = (2, 4)

p = 5

initial_w1 = 0
initial_w2 = 0


def delta(y, p):
	return int(p - y)


def func(w1, w2, point):
	return point[0] * w1 + point[1] * w2


def update(w, x, delta):
	return w + delta * x * sigma


def check(w1, w2):
	y1 = func(w1, w2, x1)
	y2 = func(w1, w2, x2)
	return (y1 > p) and (y2 < p)


def learn_first(w1, w2):
	if check(w1, w2):
		return [w1, w2]
	else:
		y = func(w1, w2, x1)
		d = delta(y, p)
		return learn_second(update(w1, x1[0], d), update(w2, x1[1], d))


def learn_second(w1, w2):
	if check(w1, w2):
		return [w1, w2]
	else:
		y = func(w1, w2, x2)
		d = delta(y, p)
		return learn_first(update(w1, x2[0], d), update(w2, x2[1], d))


res = learn_first(initial_w1, initial_w2)

print("w1 = " + str(res[0]))
print("w2 = " + str(res[1]))
