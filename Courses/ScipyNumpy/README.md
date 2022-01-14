# Numpy cheat sheet


### Creation: vector cases

For the random part, one is expected to run a command like
```Python
rng = np.random.default_rng(12)
```
before anything, to call the generator `rng`.


| Code                 | Result        |
|----------------------|-----------|
| <pre> x = np.zeros(9) </pre>         | <image src = "./CheatSheet/figures/create-zeros-1.png" width="100px"></image>        |
| `x = np.ones(9)`          | <image src = "./CheatSheet/figures/create-ones-1.png" width="100px"></image>         |
| `x = np.full(9, 0.5)`          | <image src = "./CheatSheet/figures/create-full-1.png" width="100px"></image>         |
| `x = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0])` |  <image src = "./CheatSheet/figures/create-list-1.png" width="100px"></image>|
| `x = np.arange(9)`        | <image src = "./CheatSheet/figures/create-arange-1.png" width="100px"></image>           |
| `x = rng.random(9)`        | <image src = "./CheatSheet/figures/create-uniform-1.png" width="100px"></image>           |


### Creation: matrix cases


| Code                 | Result        |
|----------------------|-----------|
| `M = np.zeros((5, 9))`    |   <image src = "./CheatSheet/figures/create-zeros-2.png" width="200px"></image> |
|`M = np.ones((5, 9))` |  <image src = "./CheatSheet/figures/create-ones-2.png" width="200px"></image> |
|`M = np.array(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`[`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[0.0, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`<br>&nbsp;&nbsp;&nbsp;&nbsp;`]`<br>`)`</code> | <image src = "./CheatSheet/figures/create-list-2.png" width="200px"></image> |
|`M = arange(5 * 9).reshape(5, 9)` | <image src = "./CheatSheet/figures/create-arange-2.png" width="200px"></image>|
| `M = rng.random(9)`        | <image src = "./CheatSheet/figures/create-uniform-2.png" width="200px"></image>           |
| `M = np.eye(5, 9)`        | <image src = "./CheatSheet/figures/create-eye-2.png" width="200px"></image>           |
| `M = np.diag(np.arange(5))`        | <image src = "./CheatSheet/figures/create-diag-2.png" width="200px"></image>           |
| `M = np.diag(np.arange(3), k=2)`        | <image src = "./CheatSheet/figures/create-diagk-2.png" width="200px"></image>           |



### Creation: tensor cases

| Code                 | Result        |
|----------------------|-----------|
| `T = np.zeros((3, 5, 9))`         |  <image src = "./CheatSheet/figures/create-zeros-3.png" width="200px"></image>        |
| `T = np.ones((3, 5, 9))`         |  <image src = "./CheatSheet/figures/create-ones-3.png" width="200px"></image>        |
| `T = np.arange(3 * 5 * 9).reshape(3, 5, 9)`         |  <image src = "./CheatSheet/figures/create-arange-3.png" width="200px"></image>        |
| `T = rng.random((3, rows, cols))`         |  <image src = "./CheatSheet/figures/create-uniform-3.png" width="200px"></image>        |


## Resources
- This work is deeply inspired and adapted from the great work by Nicolas Rougier: [https://github.com/rougier/numpy-tutorial](https://github.com/rougier/numpy-tutorial)


