import random as rnd

# Реализации составления пар в популяции
import numpy as np


class ParentSelector:
    def __init__(self, count):
        self.count = count

    def select(self, population):
        pass


class Panmixia(ParentSelector):
    def __init__(self, count):
        super().__init__(count)

    def select(self, population):
        return [(i, rnd.randint(0, self.count - 1)) for i in range(self.count)]


class Inbreeding(ParentSelector):
    def __init__(self, count):
        super().__init__(count)

    def get_close(self, population, number):
        m = 0
        min_v = float('+inf')
        for i in range(self.count):
            value = np.linalg.norm(population[number] - population[i])
            if i != number and value < min_v:
                m = i
                m_v = min_v
        return i

    def select(self, population):
        result = []
        for i in range(self.count):
            r = rnd.randint(0, self.count - 1)
            result.append((r, self.get_close(population, r)))
        return result


class TournamentSelection(ParentSelector):
    def __init__(self, count, t, f):
        super().__init__(count)
        self.t = t
        self.f = f

    def select(self, population):
        result = []
        for i in range(self.count):
            data = rnd.choices(population=population, k=self.t)
            best = sorted(data, key=self.f, reverse=True)[0]
            result.append(best)
        return result
