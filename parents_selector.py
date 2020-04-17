import random as rnd


# Реализации составления пар в популяции
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
