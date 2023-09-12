# Code adapted from :
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
        d = 0.3 * (i - 0.5) / float(Z.shape[0])
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


# %%
# Vectors

rows, cols = 5, 9

x = np.array([0.0, 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) + 0.1
show_array2(x, "create-list-1.svg")

x = np.zeros(cols) + 0.1
show_array2(x, "create-zeros-1.svg")

x = np.full(cols, 0.5)
show_array2(x, "create-full-1.svg")

x = np.ones(cols) + 0.1
show_array2(x, "create-ones-1.svg")

x = np.arange(cols)
show_array2(x, "create-arange-1.svg")

x = rng.random(cols)
show_array2(x, "create-uniform-1.svg")

# %%
# Matrices

M = np.zeros((rows, cols)) + 0.1
show_array2(M, "create-zeros-2.svg")

M = np.ones((rows, cols)) + 0.1
show_array2(M, "create-ones-2.svg")

M = np.array(
    [
        [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]
)
M += 0.1
show_array2(M, "create-list-2.svg")

M = np.arange(rows * cols).reshape(rows, cols) + 0.1
show_array2(M, "create-arange-2.svg")

M = rng.random((rows, cols))
show_array2(M, "create-uniform-2.svg")

M = np.eye(rows, cols) + 0.1
show_array2(M, "create-eye-2.svg")

M = np.diag(np.arange(5)) + 0.1
show_array2(M, "create-diag-2.svg")

M = np.diag(np.arange(3), k=1) + 0.1
show_array2(M, "create-diagk-2.svg")

# %%
# Tensors
T = np.zeros((3, 5, 9)) + 0.1
show_array3(T, "create-zeros-3.svg")

T = np.ones((3, 5, 9)) + 0.1
show_array3(T, "create-ones-3.svg")

T = np.arange(3 * 5 * 9).reshape(3, 5, 9)
show_array3(T, "create-arange-3.svg")

T = rng.random((3, rows, cols))
show_array3(T, "create-uniform-3.svg")

# %%
# Tensor constant per slice, and linearly increasing over the 3rd axis.)
n_samples_max, n_repetitions_max = 5, 3
my_ones = np.ones((n_repetitions_max, n_samples_max))
my_ones = my_ones[:, :, np.newaxis]
p_tensor = my_ones * np.linspace(0.01, 0.99, num=8)
show_array3(p_tensor, "create-increasing-slice.svg")


# %%
# Slicing:

rows, cols = 3, 4

M = np.zeros((rows, cols)) + 0.1
M[2, 2] = 1
show_array2(M, "reshape-M.svg")

M = M.reshape(4, 3)
show_array2(M, "reshape-M-reshape(4,3).svg")

M = M.reshape(12, 1)
show_array2(M, "reshape-M-reshape(12,1).svg")

M = M.reshape(1, 12)
show_array2(M, "reshape-M-reshape(1,12).svg")

M = M.reshape(6, 2)
show_array2(M, "reshape-M-reshape(6,2).svg")

M = M.reshape(2, 6)
show_array2(M, "reshape-M-reshape(2,6).svg")

# %%
# Slicing

rows, cols = 5, 9

M = np.zeros((rows, cols)) + 0.1
show_array2(M, "slice-M.svg")

M = np.zeros((rows, cols)) + 0.1
M[...] = 1
show_array2(M, "slice-M[...].svg")

M = np.zeros((rows, cols)) + 0.1
M[:, ::2] = 1
show_array2(M, "slice-M[:,::2].svg")

M = np.zeros((rows, cols)) + 0.1
M[::2, :] = 1
show_array2(M, "slice-M[::2,:].svg")

M = np.zeros((rows, cols)) + 0.1
M[1, 1] = 1
show_array2(M, "slice-M[1,1].svg")

M = np.zeros((rows, cols)) + 0.1
M[:, 0] = 1
show_array2(M, "slice-M[:,0].svg")

M = np.zeros((rows, cols)) + 0.1
M[0, :] = 1
show_array2(M, "slice-M[0,:].svg")

M = np.zeros((rows, cols)) + 0.1
M[2:, 2:] = 1
show_array2(M, "slice-M[2:,2:].svg")

M = np.zeros((rows, cols)) + 0.1
M[:-2, :-2] = 1
show_array2(M, "slice-M[:-2,:-2].svg")

M = np.zeros((rows, cols)) + 0.1
M[2:4, 2:4] = 1
show_array2(M, "slice-M[2:4,2:4].svg")

M = np.zeros((rows, cols)) + 0.1
M[::2, ::2] = 1
show_array2(M, "slice-M[::2,::2].svg")

M = np.zeros((rows, cols)) + 0.1
M[3::2, 3::2] = 1
show_array2(M, "slice-M[3::2,3::2].svg")

# %%
# Operations

rows, cols = 3, 6
M = np.linspace(0, 1, rows * cols).reshape(rows, cols)

show_array2(M, "Operations-M.svg")

show_array2(np.where(M.copy() > 0.5, 0, 1), "Operations-where.svg")

show_array2(np.maximum(M.copy(), 0.5), "Operations-max.svg")

show_array2(np.minimum(M.copy(), 0.5), "Operations-min.svg")

show_array2(np.mean(M.copy(), axis=0), "Operations-mean0.svg")

show_array2(np.mean(M.copy(), axis=1), "Operations-mean1.svg")


# %%
# Broadcasting
rows, cols = 3, 6
M = rng.random((rows, cols)) / 2
show_array2(M, "Broadcast-M.svg")

show_array2(0.5, "Broadcast-scalar.svg")
show_array2(M + 0.5, "Broadcast-scalar-res.svg")

op = np.linspace(0, 1, cols).reshape(1, cols)
show_array2(op, "Broadcast-row.svg")
show_array2(M + op, "Broadcast-row-res.svg")


op = np.linspace(0, 1, rows).reshape(rows, 1)
show_array2(op, "Broadcast-col.svg")
show_array2(M + op, "Broadcast-col-res.svg")

op_col = np.linspace(0, 1, cols).reshape(1, cols)
show_array2(op_col, "Broadcast-col2.svg")

op_row = np.linspace(0, 1, rows).reshape(rows, 1)
show_array2(op_row, "Broadcast-row2.svg")

show_array2(op_col + op_row, "Broadcast-col-row.svg")
#  %%
# Meshgrid
nx, ny = (8, 3)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
show_array2(x, "meshgrid-x.svg")
show_array2(y, "meshgrid-y.svg")

show_array2(xv, "meshgrid-xv.svg")
show_array2(yv, "meshgrid-yv.svg")

# %%
