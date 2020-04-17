import numpy as np
import matplotlib.pyplot as plt


def get_cubic_grid(dim, min_value, max_value, grid_ann):
    """
    Creates the uniform cubic grid
    :param dim: dimension of the cube
    :param grid_ann: axis notes number - notes number of the grid on each axis
    :param min_value: minimum value for each axis
    :param max_value: maximum value for each axis
    :return: numpy array of notes of the uniform cubic grid
    """
    diameter = (max_value - min_value) / grid_ann
    grid = np.zeros((grid_ann ** dim, dim))

    for i in range(grid_ann ** dim):
        _i = i
        for j in range(dim):
            grid[i][j] = min_value + diameter * (_i % grid_ann + 0.5)
            _i //= grid_ann

    return grid


def get_circle_grid(dim, radius, grid_ann):
    """
    Creates the uniform circle grid
    :param dim: dimension of the circle
    :param radius: radius of the circle
    :param grid_ann: axis notes number
    :return: numpy array of notes of the uniform circle grid
    """
    cubic_grid = get_cubic_grid(dim, -radius, radius, grid_ann)
    # return np.array([value for value in cubic_grid if np.linalg.norm(value) <= radius])
    return cubic_grid


def show_func_single_variable(func, radius):
    G_grid = get_circle_grid(dim=1, radius=radius, grid_ann=100)
    psi_grid = np.array([func(G_grid[i]) for i in range(len(G_grid))])

    plt.plot(G_grid, psi_grid)
    plt.show()


def plot_3D(G_grid, f_grid, G_grid_ann):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(G_grid[:, 0].reshape(G_grid_ann, G_grid_ann),
                    G_grid[:, 1].reshape(G_grid_ann, G_grid_ann),
                    f_grid.reshape(G_grid_ann, G_grid_ann))


def show_func_two_variable(func, radius):
    G_grid_ann = 30
    G_grid = get_circle_grid(dim=2, radius=radius, grid_ann=G_grid_ann)
    psi_grid = np.array([func(*G_grid[i]) for i in range(len(G_grid))])

    plot_3D(G_grid, psi_grid, G_grid_ann)
    plt.show()
