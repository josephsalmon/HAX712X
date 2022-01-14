# code adapted from :
# https://github.com/rougier/numpy-tutorial

# %%
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(12)

sides = ["top", "bottom", "right", "left"]


def show_array2(Z, name):
    Z = np.atleast_2d(Z)
    rows, cols = Z.shape
    fig = plt.figure(dpi=72)
    fig.figsize = (cols / 4.0, rows / 4.0)
    ax = plt.subplot(111)
    plt.imshow(
        Z,
        cmap="Oranges",
        extent=[0, cols, 0, rows],
        vmin=0,
        vmax=max(1, Z.max()),
        interpolation="nearest",
        origin="upper",
    )
    plt.xticks([]), plt.yticks([])
    for pos in sides:
        ax.spines[pos].set_edgecolor("k")
        ax.spines[pos].set_alpha(0.25)
    plt.savefig("figures/%s" % name, dpi=72)


def show_array3(Z, name):
    Z = np.atleast_2d(Z)
    rows, cols = Z.shape[1], Z.shape[2]
    fig = plt.figure(figsize=(cols, rows), dpi=72, frameon=False)
    for i in range(Z.shape[0], 0, -1):
        d = 0.5 * i / float(Z.shape[0])
        ax = plt.axes([d, d, 0.7, 0.7])
        plt.imshow(
            Z[Z.shape[0] - i],
            cmap="Oranges",
            extent=[0, cols, 0, rows],
            vmin=0,
            vmax=max(1, Z.max()),
            interpolation="nearest",
            origin="upper",
        )
        plt.xticks([]), plt.yticks([])
        for pos in sides:
            ax.spines[pos].set_edgecolor("k")
            ax.spines[pos].set_alpha(0.25)
    plt.savefig("figures/%s" % name, dpi=16)


# Vectors

rows, cols = 5, 9

x = np.array([0.0, 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) + 0.1
show_array2(x, "create-list-1.png")

x = np.zeros(cols) + 0.1
show_array2(x, "create-zeros-1.png")

x = np.ones(cols) + 0.1
show_array2(x, "create-ones-1.png")

x = np.arange(cols)
show_array2(x, "create-arange-1.png")

x = rng.random(0, 1, cols)
show_array2(x, "create-uniform-1.png")


# Matrices

M = np.zeros((rows, cols)) + 0.1
show_array2(M, "create-zeros-2.png")

M = np.ones((rows, cols)) + 0.1
show_array2(M, "create-ones-2.png")

M = np.array(
    [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]
)
M += 0.1
show_array2(M, "create-list-2.png")

M = np.arange(rows * cols).reshape(rows, cols)
show_array2(M, "create-arange-2.png")

M = np.random.uniform(0, 1, (rows, cols))
show_array2(M, "create-uniform-2.png")


# Tensors
T = np.zeros((3, 5, 9)) + 0.1
show_array3(T, "create-zeros-3.png")

T = np.ones((3, 5, 9)) + 0.1
show_array3(T, "create-ones-3.png")

T = np.arange(3 * 5 * 9).reshape(3, 5, 9)
show_array3(T, "create-arange-3.png")

T = np.random.uniform(0, 1, (3, rows, cols))
show_array3(T, "create-uniform-3.png")

# %%
