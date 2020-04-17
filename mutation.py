import random as rnd

import numpy as np


# Руализация функций мутации
class Mutation:
    def __init__(self, delta):
        self.delta = delta

    def mutate(self, x):
        pass


class SimpleMutation(Mutation):
    def __init__(self, delta, probability):
        super().__init__(delta)
        self.probability = probability

    def mutate(self, x):
        new_x = []
        for i in range(len(x)):
            if rnd.random() <= self.probability:
                new_x.append(x[i] + self.delta * (-1 if rnd.random() <= 0.5 else 1))
            else:
                new_x.append(x[i])
        return np.array(new_x)


class HeterogeneousMutation(Mutation):
    def __init__(self, delta, min_value, max_value, population_count, b):
        super().__init__(delta)
        self.min_value = min_value
        self.max_value = max_value
        self.T = population_count
        self.b = b

    def mutate(self, y, t):
        new_y = []
        for i in range(len(y)):
            q = rnd.randint(0, 1)
            r = rnd.random()
            p = (1 - r ** ((1 - t / self.T) ** self.b))
            if q == 0:
                new_y.append(y[i] + (self.max_value - y[i]) * p)
            else:
                new_y.append(y[i] - (y[i] - self.min_value) * p)
        return np.array(new_y)
