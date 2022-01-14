# Numpy and scipy


## Numpy cheat sheet


### Creation: vector cases

For the random part, one is expected to run a command like
```Python
rng = np.random.default_rng(12)
```
before anything, to call the generator `rng`.


| Code                 | Result        |
|----------------------|-----------|
| x = np.zeros(9)         | <image src = "./CheatSheet/figures/create-zeros-1.png" width="100px"></image>        |
| x = np.ones(9)          | <image src = "./CheatSheet/figures/create-ones-1.png" width="100px"></image>         |
| x = np.full(9, 0.5)          | <image src = "./CheatSheet/figures/create-full-1.png" width="100px"></image>         |
| x = np.array([0,0,1,0,0,0,0,0,0] ) |  <image src = "./CheatSheet/figures/create-list-1.png" width="100px"></image>|
| x = np.arange(9)        | <image src = "./CheatSheet/figures/create-arange-1.png" width="100px"></image>           |
| x = rng.random(9)        | <image src = "./CheatSheet/figures/create-uniform-1.png" width="100px"></image>           |


### Creation: matrix cases


| Code                 | Result        |
|----------------------|-----------|
| M = np.zeros((5, 9))    |   <image src = "./CheatSheet/figures/create-zeros-2.png" width="100px"></image>       |
| M = np.ones((5, 9))          |  <image src = "./CheatSheet/figures/create-ones-2.png" width="100px"></image>       |


### Creation: tensor cases

| Code                 | Result        |
|----------------------|-----------|
| Z = zeros(9)         |         |
| Z = ones(9)          |         |



## Resources
- Inspiration from the great work by Nicolas Rougier: https://github.com/rougier/numpy-tutorial


