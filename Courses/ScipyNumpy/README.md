# Numpy cheat sheet


## Matrix creation

### Creation: vector cases

For the random part, one is expected to run a command like
```Python
rng = np.random.default_rng(12)
```
before anything, to call the generator `rng`.


| Code                 | Result        |
|----------------------|-----------|
| <pre> x = np.zeros(9) </pre>         | <image src = "./CheatSheet/figures/create-zeros-1.svg" width="200px"></image>        |
| <pre> x = np.ones(9)</pre>          | <image src = "./CheatSheet/figures/create-ones-1.svg" width="200px"></image>         |
| <pre> x = np.full(9, 0.5)</pre>          | <image src = "./CheatSheet/figures/create-full-1.svg" width="200px"></image>         |
| <pre> x = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0])</pre> |  <image src = "./CheatSheet/figures/create-list-1.svg" width="200px"></image>|
| <pre> x = np.arange(9)</pre>        | <image src = "./CheatSheet/figures/create-arange-1.svg" width="200px"></image>           |
| <pre> x = rng.random(9)</pre>        | <image src = "./CheatSheet/figures/create-uniform-1.svg" width="200px"></image>           |


### Creation: matrix cases


| Code                 | Result        |
|----------------------|-----------|
|<pre>M = np.ones((5, 9)) </pre> | <image src = "./CheatSheet/figures/create-ones-2.svg" width="200px"></image> |
|<pre>M = np.zeros((5, 9))</pre> | <image src = "./CheatSheet/figures/create-zeros-2.svg" width="200px"></image> |
|<pre> M = np.array(<br>&nbsp;&nbsp;&nbsp;&nbsp;[<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]<br>&nbsp;&nbsp;&nbsp;&nbsp;]<br>)</pre>|<image src = "./CheatSheet/figures/create-list-2.svg" width="200px"></image>
|<pre> M = arange(5 * 9).reshape(5, 9)</pre> | <image src = "./CheatSheet/figures/create-arange-2.svg" width="200px"></image>|
|<pre> M = rng.random(9)</pre>        | <image src = "./CheatSheet/figures/create-uniform-2.svg" width="200px"></image>           |
|<pre> M = np.eye(5, 9)</pre>        | <image src = "./CheatSheet/figures/create-eye-2.svg" width="200px"></image>           |
|<pre> M = np.diag(np.arange(5)) </pre>        | <image src = "./CheatSheet/figures/create-diag-2.svg" width="200px"></image>           |
|<pre> M = np.diag(np.arange(3), k=2) </pre>        | <image src = "./CheatSheet/figures/create-diagk-2.svg" width="200px"></image>           |



### Creation: tensor cases

| Code                 | Result        |
|----------------------|-----------|
| <pre>T = np.zeros((3, 5, 9))</pre>         |  <image src = "./CheatSheet/figures/create-zeros-3.svg" width="200px"></image>        |
| <pre>T = np.ones((3, 5, 9))</pre>         |  <image src = "./CheatSheet/figures/create-ones-3.svg" width="200px"></image>        |
| <pre>T = np.arange(3 * 5 * 9).reshape(3, 5, 9)</pre>         |  <image src = "./CheatSheet/figures/create-arange-3.svg" width="200px"></image>        |
| <pre>T = rng.random((3, rows, cols))</pre>         |  <image src = "./CheatSheet/figures/create-uniform-3.svg" width="200px"></image>        |



## Matrix reshaping
We start here with
```Python
M = np.zeros((3, 4))
M[2, 2] = 1
```

<image src = "./CheatSheet/figures/reshape-M.svg" width="200px"></image> 


| Code                 | Result        |
|----------------------|-----------|
| <pre>M = M.reshape(4, 3)</pre>         |  <image src = "./CheatSheet/figures/reshape-M-reshape(4,3).svg" width="200px"></image>        |
| <pre>M = M.reshape(12, 1)</pre>         |  <image src = "./CheatSheet/figures/reshape-M-reshape(12,1).svg" width="200px"></image>        |
| <pre>M = M.reshape(1, 12)</pre>         |  <image src = "./CheatSheet/figures/reshape-M-reshape(1,12).svg" width="200px"></image>        |
| <pre>M = M.reshape(6, 2)</pre>         |  <image src = "./CheatSheet/figures/reshape-M-reshape(6,2).svg" width="200px"></image>        |
| <pre>M = M.reshape(2, 6)</pre>         |  <image src = "./CheatSheet/figures/reshape-M-reshape(2,6).svg" width="200px"></image>        |



## Slicing

Start from a zero matrix:
```Python
M = np.zeros((5, 9))
```

<image src = "./CheatSheet/figures/slice-M.svg" width="200px"></image> 


| Code                 | Result        |
|----------------------|-----------|
| <pre>M[...] = 1 </pre>         |  <image src = "./CheatSheet/figures/slice-M[...].svg" width="200px"></image>        |
| <pre>M[:, ::2] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[:,::2].svg" width="200px"></image>        |
| <pre>M[::2, :] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[::2,:].svg" width="200px"></image>        |
| <pre>M[1, 1] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[1,1].svg" width="200px"></image>        |
| <pre>M[:, 0] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[:,0].svg" width="200px"></image>        |
| <pre>M[0, :] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[0,:].svg" width="200px"></image>        |
| <pre>M[2:, 2:] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[2:,2:].svg" width="200px"></image>        |
| <pre>M[:-2, :-2] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[:-2,:-2].svg" width="200px"></image>        |
| <pre>M[2:4, 2:4] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[2:4,2:4].svg" width="200px"></image>        |
| <pre>M[::2, ::2] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[::2,::2].svg" width="200px"></image>        |
| <pre>M[3::2, 3::2] = 1</pre>         |  <image src = "./CheatSheet/figures/slice-M[3::2,3::2].svg" width="200px"></image>        |


## Resources
- This work is deeply inspired and adapted from the great work by Nicolas Rougier: [https://github.com/rougier/numpy-tutorial](https://github.com/rougier/numpy-tutorial)


