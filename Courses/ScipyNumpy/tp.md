 # SciPy - scientific library in `python`

    Joseph Salmon : joseph.salmon@umontpellier.fr

 Adapted from

 - A. Gramfort (alexandre.gramfort@inria.fr) http://alexandre.gramfort.net/
 - J.R. Johansson (robert@riken.jp) http://dml.riken.jp/~rob/

 ## Introduction

 SciPy build upon NumPy.


 Among others, SciPy deals with:

* Integration ([scipy.integrate](http://docs.scipy.org/doc/scipy/reference/integrate.html))
* Optimization ([scipy.optimize](http://docs.scipy.org/doc/scipy/reference/optimize.html))
* Interpolation ([scipy.interpolate](http://docs.scipy.org/doc/scipy/reference/interpolate.html))
* Fourier Transform ([scipy.fftpack](http://docs.scipy.org/doc/scipy/reference/fftpack.html))
* Signal Processing ([scipy.signal](http://docs.scipy.org/doc/scipy/reference/signal.html))
* Linear Algebra ([scipy.linalg](http://docs.scipy.org/doc/scipy/reference/linalg.html))
* *Sparse* matrices ([scipy.sparse](http://docs.scipy.org/doc/scipy/reference/sparse.html))
* Statistics ([scipy.stats](http://docs.scipy.org/doc/scipy/reference/stats.html))
* Image processing ([scipy.ndimage](http://docs.scipy.org/doc/scipy/reference/ndimage.html))
* IO (input/output) ([scipy.io](http://docs.scipy.org/doc/scipy/reference/io.html))


```python
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
```

# Animation display with `python`

## Animation with `matplotlib`
VSCode backend cannot handle the example out of the box...
Use that one in a terminal.

```python
fig, ax = plt.subplots()
xdata, ydata = [], []
(ln,) = plt.plot([], [], "ro")


def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return (ln,)


def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return (ln,)


ani = FuncAnimation(
    fig, update, frames=np.linspace(0, 2 * np.pi, 128), init_func=init, blit=True
)
plt.show()
```

Yet,  a workaround exists:
from IPython.display import HTML

```python
HTML(ani.to_jshtml())
```

# Animation with `plotly'
`matplotlib` works fine for advance tuning, but is harder for simple tasks.
So just try `plotly` for basic animations:

```python
import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder()
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90],
)
fig.show("notebook")
```

 ## Linear algebra

 `scipy` for linear algebra : use `linalg`. It includes function for solving
 lineair systems, eigen value decomposition, SVD, Gaussian elimination (LU, Cholesky), etc.

 Documentation : http://docs.scipy.org/doc/scipy/reference/linalg.html

#### Solving linear systems:
Find $x$ such that: $A x = b$
for specified matrix $A$ and vector $b$.

```python
 A = np.array([[1, 0, 3], [4, 5, 12], [7, 8, 9]], dtype=np.float)
# A = np.random.randn(500, 500)
# b = np.ones((500, 1))
b = np.array([[1, 2, 3]], dtype=np.float64).T
# b = np.array([[1, 2, 3]], dtype=np.float64).T

print(A)
print(b)

x = linalg.solve(A, b)
print(x)
print(x.shape)
print(b.shape)
```


Check the result at given precision (different from ==)

```python
np.allclose(A @ x, b, atol=1e-14, rtol=1e-15)
```
**Remark**: NEVER (or you should really know why) invert a matrix.
**ALWAYS** solve linear systems instead!

#### Eigen values / vectors

$A v_n = \lambda_n v_n$ with $v_n$ the $n$-th eigen vector and $\lambda_n$ the $n$-th eigen value. The associated `python` functions are `eigvals` abd `eig`:

```python
A = np.random.randn(3, 3)
A = A + A.T
evals, evecs = linalg.eig(A)
print(evals, "\n ------\n", evecs)

# V = [v_1, ... v_n] , columns = eigen vectors
# A = V diag(s_1,...,s_n) V^T

np.allclose(A, evecs @ np.diag(evals) @ evecs.T)

```
### <font color='red'> EXERCISE : Eigen values/vectors</font>

Verify numerically that the output from `linalg.eig` are indeed approximately
eigen values and eigen vectors of the matrix A above.

*Hint* : use https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html

# If A is symmetric you **should** use `eigvalsh` (H for Hermitian) instead:
# this is more robust, and leverages the structures (you know they are real!)

# %%


# #### Matrix operations
# %%
linalg.inv(A)  # Inversion, consider NEVER using it though  :)
linalg.det(A)  # determinant

# normes
print(linalg.norm(A, ord="fro"))  # fro for Frobenius
print((np.sum(A ** 2)) ** 0.5)
print(linalg.norm(A, ord=2))
print((linalg.eigvalsh(A.T @ A) ** 0.5))
print(linalg.norm(A, ord=np.inf))


### <font color='red'> EXERCISE : Norms computation</font>
Check numerically what is the instruction  `linalg.norm(A, ord=np.inf)`
really computing.
Double check with the help, and a numerical test.


```python
A = np.random.randn(3, 3)
print(linalg.norm(A, ord=np.inf))
```

# Random generation, distributions, etc.
(see more on this at <https://albertcthomas.github.io/good-practices-random-number-generators/> or <https://numpy.org/doc/1.18/reference/random/legacy.html#numpy.random.RandomState>)

```python
seed = 12345
rng = np.random.default_rng(seed)  # can be called without a seed
rng.random()

```

Visualization of the various possible distribution are available here (see widgets): <https://github.com/josephsalmon/Random-Widgets>


## Optimization
**Goal**: find functions minima or maxima
Doc : http://scipy-lectures.github.com/advanced/mathematical_optimization/index.html


```python
from scipy import optimize
```
### Find a (local!) minima;

```python
def f(x):
    return 4 * x ** 3 + (x - 2) ** 2 + x ** 4


def mf(x):
    return -(4 * x ** 3 + (x - 2) ** 2 + x ** 4)


xs = np.linspace(-5, 3, 100)
plt.figure()
plt.plot(xs, f(xs))
plt.show()
```

# `fmin_bfgs` (see https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)


```python
x_min = optimize.fmin_bfgs(f, x0=-4)
x_max = optimize.fmin_bfgs(mf, x0=-2)
x_min2 = optimize.fmin_bfgs(f, x0=2)


plt.figure()
plt.plot(xs, f(xs))
plt.plot(x_min, f(x_min), "o", markersize=10, color="orange")
plt.plot(x_min2, f(x_min2), "o", markersize=10, color="red")
plt.plot(x_max, f(x_max), "|", markersize=20)
plt.show()



```

### <font color='red'> EXERCISE : Bassin of attraction</font>
Draw the points on the curves with 2 different colors :
- orange for the points leading to find the left local minima
- red for the points leading to the right local minima.

### Find the zeros of a function
Find $x$ such that $f(x) = 0$, with `fsolve`.

```python
omega_c = 3.0

def f(omega):
    return np.tan(2 * np.pi * omega) - omega_c / omega



x = np.linspace(1e-8, 3.2, 1000)
y = f(x)

# remove vertical lines when the function flips sign
mask = np.where(np.abs(y) > 50)
x[mask] = y[mask] = np.nan
plt.plot(x, y)
plt.plot([0, 3.3], [0, 0], "k")
plt.ylim(-5, 5)

optimize.fsolve(f, 0.72)
optimize.fsolve(f, 1.1)
optimize.fsolve(f, np.linspace(0.001, 3, 20))
np.unique(np.round(optimize.fsolve(f, np.linspace(0.2, 3, 20)), 3))

my_zeros = (
    np.unique((optimize.fsolve(f, np.linspace(0.2, 3, 20)) * 1000).astype(int)) / 1000.0
)
plt.figure()
plt.plot(x, y, label="$f$")
plt.plot([0, 3.3], [0, 0], "k")
plt.plot(my_zeros, np.zeros(my_zeros.shape), "o", label="$x : f(x)=0$")
plt.legend()
plt.show()
```


#### Parameters estimation

```python
from scipy.optimize import curve_fit


def f(x, a, b, c):
    """f(x) = a exp(-bx) + c."""
    return a * np.exp(-b * x) + c


x = np.linspace(0, 4, 50)
y = f(x, 2.5, 1.3, 0.5)  # true signal
yn = y + 0.2 * np.random.randn(len(x))  # noisy added


plt.figure()
plt.plot(x, yn, ".")
plt.plot(x, y, "k", label="$f$")
plt.legend()


(a, b, c), _ = curve_fit(f, x, yn)
print(a, b, c)

# curve_fit?
```

Displaying

```python
plt.figure()
plt.plot(x, yn, ".", label="data")
plt.plot(x, y, "k", label="True $f$")
plt.plot(x, f(x, a, b, c), "--k", label="Estimated $\hat{f}$")
plt.legend()
plt.show()
```

Rem: for polynomial one can directly use `numpy`

```python
x = np.linspace(0, 1, 10)
y = np.sin(x * np.pi / 2.0)
line = np.polyfit(x, y, deg=10)
plt.figure()
plt.plot(x, y, ".", label="data")
plt.plot(x, np.polyval(line, x), "k--", label="polynomial approximation")
plt.legend()
plt.show()
```


## Interpolation

```python
from scipy.interpolate import interp1d, CubicSpline


def f(x):
    return np.sin(x)


n = np.arange(0, 10)
x = np.linspace(0, 9, 100)

y_meas = f(n) + 0.1 * np.random.randn(len(n))  # add noise
y_real = f(x)

linear_interpolation = interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cubic_interpolation = CubicSpline(n, y_meas)
y_interp2 = cubic_interpolation(x)


plt.figure()
plt.plot(n, y_meas, "bs", label="noisy data")
plt.plot(x, y_real, "k", lw=2, label="true function")
plt.plot(x, y_interp1, "r", label="linear interp")
plt.plot(x, y_interp2, "g", label="CubicSpline interp")
plt.legend(loc=3)
plt.show()
```


### Images

```python
from scipy import ndimage, misc

img = misc.face()
type(img), img.dtype, img.ndim, img.shape


print(2 ** 8)  # uint8-> code sur 256 niveau.

n_1, n_2, n_3 = img.shape
np.unique(img)


# True image
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.show()
```

### RGB decomposition

```python
fig, ax = plt.subplots(3, 2)
fig.set_size_inches(9, 6.5)
n_1, n_2, n_3 = img.shape

ax[0, 0].imshow(img[:, :, 0], cmap=plt.cm.Reds)
ax[0, 1].hist(img[:, :, 0].reshape(n_1 * n_2), np.arange(0, 256))

ax[1, 0].imshow(img[:, :, 1], cmap=plt.cm.Greens)
ax[1, 1].hist(img[:, :, 1].reshape(n_1 * n_2), np.arange(0, 256))

ax[2, 0].imshow(img[:, :, 2], cmap=plt.cm.Blues)
ax[2, 1].hist(img[:, :, 2].reshape(n_1 * n_2), np.arange(0, 256))

plt.tight_layout()
```


```python
print(img.flags)  # cannot edit...
img_compressed = img.copy()
img_compressed.setflags(write=1)
print(img_compressed.flags)  # can edit now


img_compressed[img_compressed < 70] = 50
img_compressed[(img_compressed >= 70) & (img_compressed < 110)] = 100
img_compressed[(img_compressed >= 110) & (img_compressed < 180)] = 150
img_compressed[(img_compressed >= 180)] = 200
plt.figure()
plt.imshow(img_compressed, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
```

### Convert a color image in grayscale

```python
plt.figure()
plt.imshow(np.mean(img, axis=2), cmap=plt.cm.gray)
plt.show()
```
### Blurring (fr: floutage)

# Blurring (fr: floutage)



```python
img_flou = ndimage.gaussian_filter(img, sigma=20)
fix, ax = plt.subplots()
ax.imshow(img_flou, cmap=plt.cm.gray)
ax.axis("off")
plt.show()

```

Widget on blurring bandwidth:

```python
%matplotlib widget
import ipywidgets as widgets

# set up plot
img_flou = ndimage.gaussian_filter(img, sigma=20)
fix, ax = plt.subplots()
ax.axis("off")
plt.show()
 
@widgets.interact(sigma=(0.1, 200, 0.1))
def update(sigma=2):
    """Remove old lines from plot and plot new one"""
    # [l.remove() for l in ax.lines]
    img_flou = ndimage.gaussian_filter(img, sigma)
    ax.imshow(img_flou, cmap=plt.cm.gray)

```

## Changing colors in an image

```python
import pooch
import os

url = "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/486px-Flag_of_Brazil.svg.png"
name_img =pooch.retrieve(url, known_hash=None)

img = (255 * plt.imread(name_img)).astype(int)
img = img.copy()
plt.figure()
plt.imshow(img[:, :, 2], cmap=plt.cm.gray)


fig, ax = plt.subplots(3, 2)
fig.set_size_inches(9, 6.5)
n_1, n_2, n_3 = img.shape

ax[0, 0].imshow(img[:, :, 0], cmap=plt.cm.Reds)
ax[0, 1].hist(img[:, :, 0].reshape(n_1 * n_2), np.arange(0, 256), density=True)

ax[1, 0].imshow(img[:, :, 1], cmap=plt.cm.Greens)
ax[1, 1].hist(img[:, :, 1].reshape(n_1 * n_2), np.arange(0, 256), density=True)

ax[2, 0].imshow(img[:, :, 2], cmap=plt.cm.Blues)
ax[2, 1].hist(img[:, :, 2].reshape(n_1 * n_2), np.arange(0, 256), density=True)

plt.tight_layout()
```

### <font color='red'> EXERCISE : Make the Brazilian italianer</font>
(green white red)

# XXX TODO

```python
find_white_green = img[:, :, 1] > 200

# red part
img[:, :, 0][find_dark_green] = 255

#  white part
img[:, :, 1][find_white_green] = 255

# blue part
img[:, :, 2][find_light_green] = 255

plt.imshow(img)
plt.show()
```

# More for colors/ images:
http://josephsalmon.eu/enseignement/Montpellier/HLMA310/matplotlib_slides.pdf



## Further lectures
* http://www.scipy.org - The official web page for the SciPy project.
* http://docs.scipy.org/doc/scipy/reference/tutorial/index.html - A tutorial on how to get started using SciPy.
* https://github.com/scipy/scipy/ - The SciPy source code.
* http://scipy-lectures.github.io
