import numpy as np


class TestMaximum:
    def __init__(self, func, a, b, glob_max, dim):
        self.f = func
        self.a = a
        self.b = b
        self.glob_max = glob_max
        self.dim = dim


def f1(x):
    return np.sin(4 * x)


def f2(x):
    return -(5 - 24 * x + 17 * (x ** 2) - 11 * (x ** 3) / 3 + (x ** 4) / 4)


def f3(x):
    return -(10 + (x ** 2) - 10 * np.cos(2 * np.pi * x))


def f4(x, y):
    return np.sin(6 * x) * np.cos(4 * y)


def f6(x, y):
    return np.cos(x) * np.cos(y) * np.exp(-((x - np.pi) ** 2 + (y - np.pi) ** 2))


def f7(x, y):
    return -((x * x + y - 11) ** 2 + (x + y * y - 7) ** 2)


def f8(x, y):
    return (y + 47) * np.sin(np.sqrt(np.abs(x / 2 + y + 47))) + x * np.sin(np.sqrt(np.abs(x - (y + 47))))


def f9(x, y):
    return np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - np.sqrt(x ** 2 + y ** 2) / np.pi)))


def f5(x, y, z):
    return -(10 + (x ** 2) - 10 * np.cos(2 * np.pi * x) + (
            y ** 2) - 10 * np.cos(2 * np.pi * y) + (
                     z ** 2) - 10 * np.cos(2 * np.pi * z))


TEST_1 = TestMaximum(f1, -1, 1, 0.3926, 1)
TEST_2 = TestMaximum(f2, 0, 6.5, 1, 1)
TEST_3 = TestMaximum(f3, -2, 2, 0, 1)
TEST_4 = TestMaximum(f4, -1, 1, None, 2)
TEST_5 = TestMaximum(f5, -2, 2, (0, 0, 0), 3)
TEST_6 = TestMaximum(f6, -100, 100, (np.pi, np.pi), 2)
TEST_7 = TestMaximum(f7, -5, 5, [(3, 2), (-2.8051, 3.1313), (-3.7793, -3.2831), (3.5844, -1.8481)], 2)
TEST_8 = TestMaximum(f8, -512, 512, (512, 404.2319), 2)
TEST_9 = TestMaximum(f9, -10, 10, [(8.0550, 9.6645), (-8.0550, 9.6645), (-8.0550, -9.6645), (8.0550, -9.6645)], 2)
