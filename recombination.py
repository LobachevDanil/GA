import random as rnd

import numpy as np


# Реализации функции скрещивания
class Recombination:
    def __init__(self, dim):
        self.dim = dim

    def recombine(self, x, y):
        pass


class DiscreteRecombination(Recombination):
    def __init__(self, dim):
        super().__init__(dim)

    def recombine(self, x, y):
        new_x = []
        new_y = []
        for i in range(self.dim):
            new_x.append(x[i] if rnd.random() <= 0.5 else y[i])
            new_y.append(x[i] if rnd.random() <= 0.5 else y[i])
        return np.array(new_x), np.array(new_y)


class IntermediateRecombination(Recombination):
    def __init__(self, dim):
        super().__init__(dim)
        self.d = 0.25

    def recombine(self, x, y):
        new_x = []
        new_y = []
        for i in range(self.dim):
            alpha = rnd.uniform(-self.d, 1 + self.d)
            new_x.append(x[i] + (y[i] - x[i]) * alpha)
            alpha = rnd.uniform(-self.d, 1 + self.d)
            new_y.append(x[i] + (y[i] - x[i]) * alpha)
        return np.array(new_x), np.array(new_y)


class LineRecombination(Recombination):
    def __init__(self, dim):
        super().__init__(dim)
        self.d = 0.25

    def recombine(self, x, y):
        new_x = []
        new_y = []
        alpha1 = rnd.uniform(-self.d, 1 + self.d)
        alpha2 = rnd.uniform(-self.d, 1 + self.d)
        for i in range(self.dim):
            new_x.append(x[i] + (x[i] - y[i]) * alpha1)
            new_y.append(x[i] + (x[i] - y[i]) * alpha2)
        return np.array(new_x), np.array(new_y)
