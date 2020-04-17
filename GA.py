import numpy as np

import painter
from mutation import *
from recombination import *
from parents_selector import *
from selection import *
import test_functions

ITERATION_LIMIT = 100
SELECTION_COUNT = 10


def get_random_grid(dim, min_value, max_value, grid_ann):
    """Заполняет векторы случайными значениями"""
    grid = np.zeros((grid_ann ** dim, dim))
    for i in range(grid_ann ** dim):
        for j in range(dim):
            grid[i][j] = min_value + rnd.random() * (max_value - min_value)

    return grid


def get_max(population):
    return max(population, key=f)


def run_GA(population, delta, p_m):
    former = Panmixia(len(population))
    reproducer = IntermediateRecombination(population.shape[1])
    mutation = SimpleMutation(delta, p_m)
    selector = TruncationSelection(population.shape[0], f)
    for i in range(ITERATION_LIMIT):
        pairs = former.select(population)
        size = (2 * population.shape[0], population.shape[1])
        next_generation = np.zeros(size)
        for j in range(len(pairs)):
            new_x, new_y = reproducer.recombine(
                population[pairs[j][0]], population[pairs[j][1]]
            )
            next_generation[2 * j] = mutation.mutate(new_x)
            next_generation[2 * j + 1] = mutation.mutate(new_y)
        population = selector.select(population, next_generation)
    return population


# Можно изменить номер теста, чтобы задать другую функцию
TEST = test_functions.test3


def f(x):
    return TEST.f(*x)


def main():
    ann = 20
    G_grid = get_random_grid(TEST.dim, TEST.a, TEST.b, ann)
    result = run_GA(G_grid, (TEST.b - TEST.a) / (10 * ann), 0.1)

    print('calculate local max: ', get_max(result))
    print('expected: ', TEST.glob_max)
    if TEST.dim == 1:
        painter.show_func_single_variable(TEST.f, max(abs(TEST.a), abs(TEST.b)))
    if TEST.dim == 2:
        painter.show_func_two_variable(TEST.f, max(abs(TEST.a), abs(TEST.b)))


if __name__ == "__main__":
    main()
