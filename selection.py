import numpy as np
import random as rnd


# Отбор потомков для следующей итерации
class Selection:
    def __init__(self, population_count, function):
        self.count = population_count
        self.f = function

    def select(self, parents, children):
        pass


class TruncationSelection(Selection):
    def __init__(self, population_count, function):
        super().__init__(population_count, function)

    def select(self, parents, children):
        args = np.row_stack((parents, children))
        values = [(self.f(args[i]), i) for i in range(args.shape[0])]
        data = sorted(values, key=lambda x: x[0], reverse=True)[:self.count]
        result = np.zeros(parents.shape)
        for i in range(self.count):
            result[i] = args[rnd.choice(data)[1]]
        return result


class EliteSelection(Selection):
    def __init__(self, population_count, function):
        super().__init__(population_count, function)

    def select(self, parents, children):
        args = np.row_stack((parents, children))
        values = [(self.f(args[i]), i) for i in range(args.shape[0])]
        data = sorted(values, key=lambda x: x[0], reverse=True)[:self.count]
        result = np.zeros(parents.shape)
        for i in range(self.count):
            result[i] = args[data[i][1]]
        return result
