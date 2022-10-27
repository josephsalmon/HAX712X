
# Time and memory efficiency

```python
import time
import numpy as np
import matplotlib.pyplot as plt
```


## Time / computation: usage of `%timeit`
 Other *magic*  comme are  %timeit, %matplotlib, %autoreload:
cf.
https://ipython.org/ipython-doc/3/interactive/magics.html
https://ipython.org/ipython-doc/3/config/extensions/autoreload.html

```python
n = 1000
val = 5.4
print('fill')
```

```python
%timeit a = np.empty(n); a.fill(val)
# This is a `magic` command, works only in interactive case (Ipython, Notebook, Jupyter lab etc.)
# Alternative: uncomment below
# get_ipython().run_line_magic('timeit', 'a = np.empty(n); a.fill(val)')
```

```python
print('empty')
%timeit a = np.empty(n); a[:] = val
```

```python
print('full')
```

```python
%timeit a = np.full((n,), val)
```

```python
print('ones')
```
```python
%timeit a = np.ones(n) * val
```

```python
print('repeat')
```
```python
%timeit a = np.repeat(val, n)
```


## Alternatives
Use the time module:
```import time```

```python
start = time.time()
a = np.ones(n) * val
end = time.time()
print("Temps passé pour exécuter la commande: {0:.5f} s.".format(end - start))
```



## Sparse matrices, graphs and memory
Sparse matrices are useful to to handle potentially huge matrices,
that have only few non zero coefficients.
http://scipy-lectures.org/advanced/scipy_sparse/introduction.html#why-sparse-matrices

https://rushter.com/blog/scipy-sparse-matrices/
http://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/
**Examples**:
- natural language processing: we encode the presence of a word from a
  dictionary (let's say the set of French words) and we put 0 / 1 in case of
  absence / presence of a word.
- One-hot encoding, used to represent categorical data as sparse binary
  vectors.
- the discretization of a physical system where very distant influences are
  set to zero (e.g. heat diffusion, fluid mechanics, electro/magnetism, etc.)
- graphs: graphs are naturally represented by adjacency or incidence
  matrices (cf. below), and therefore beyond the graphs, maps!


## Most common formats:
 https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse
 - coo_matrix(arg1[, shape, dtype, copy]):
   A sparse matrix in COOrdinate format.
 - csc_matrix(arg1[, shape, dtype, copy]):
   Compressed Sparse Column matrix
 - csr_matrix(arg1[, shape, dtype, copy]):
   Compressed Sparse Row matrix

```python
from scipy import sparse
from scipy.sparse import isspmatrix

Id = sparse.eye(3)
print(Id.toarray())
print(f'Q: Is the matrix Id is sparse?\nA: {isspmatrix(Id)}')

n1 = 29
n2 = 29
mat_rnd = sparse.rand(n1, n2, density=0.25, format="csr",
                      random_state=42)
print(mat_rnd.toarray())
print(f'Q: Is the matrix mat_rnd is sparse?\nA: {isspmatrix(mat_rnd)}')
```


# matrix vector product: as usual (also can use np.dot())
```python
v = np.random.rand(n2)
mat_rnd@v
```

## Graphs and sparsity
A classical framework for the application of sparse matrices is with
graphs: although the number of nodes can be huge, each node of a graph is
in general not connected to all nodes. If we represent a graph by
its adjacency matrix:

 ## Definition: *adjacency matrix*:
 Suppose that $G=(V,E)$ is a graph, where $\left|V\right|=n$.
 Suppose that the vertices of $G$ are arbitrarily numbered $v_1,\ldots,v_n.$
 The adjacency matrix $A$ of $G$ is the matrix $n \times n$ of general term:

 ```math
 A_{{i,j}}=
 \left\{
     \begin{array}{rl}
 	     1, & \text{if } (v_i,v_j) \in E \\
         0, & \text{o.w.}
      \end{array}
 \right.
```

### <font color='red'> EXERCISE : Create a linear model that can handle sparse matrices, in particular how would you do the usual pre-processing step of standardizing the columns of the design matrix?
 </font>

Usage depends on the nature and structure of the data:
 - `csc_matrix` is more efficient for `slicing` by column
 - `csr_matrix` is more efficient for the row case.


```python
import networkx as nx
nx.__version__
```

```python
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'A', weight=2)

my_seed = 44
nx.draw_networkx(G, with_labels=True,
                 pos=nx.spring_layout(G, seed=my_seed))

labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,
                             pos=nx.spring_layout(G, seed=my_seed),
                             edge_labels=labels)
nx.draw_networkx_edges(G, pos=nx.spring_layout(G, seed=my_seed),
                       width=list(labels.values()))
plt.axis('off')
plt.show()
```


### <font color='red'> EXERCISE : edges </font>
 1) show edges weights on the graph
 2) change the edge width to be proportional to the edge weights



```python
A = nx.adjacency_matrix(G)
print(isspmatrix(A))
print(A.todense())
nx.shortest_path(G, 'C', 'B', weight='weight')
```

## Definition : *incidence matrix*
Let $G = (V,E)$ be a (non-oriented) graph with $n$ vertices,
$V = [1,\dots,n]$, and $p$ edges, $E = [1,\dots,p]$.
The graph can be represented by its vertex-edge incidence matrix
$D^\top \in \mathbb{R}^{p \times n}$ defined by

```math
(D^\top)_{{e,v}} =
\left\{
     \begin{array}{rl}
    + 1, & \text{if } v = \min(i,j) \\
    -1, & \text{si } v = \max(i,j) \\
    0, & \text{sinon}
  \end{array}
  \right.
```
where $e = (i,j)$.

## Definition : *Laplacian matrix*
The matrix $L=D D^\top$ is the so-called graph Laplacian of $G$

```python
D = nx.incidence_matrix(G, oriented=True).T
print(isspmatrix(D))
print(D.todense())
```

## Interactive graph visualisation 

```python
import matplotlib.pylab as plt
g = nx.karate_club_graph()
fig, ax = plt.subplots(1, 1, figsize=(8, 6));
nx.draw_networkx(g, ax=ax)
plt.axis('off')
plt.show()
```

```
fig, ax = plt.subplots()

A = nx.adjacency_matrix(g).T

print(A.todense())
ax = plt.spy(A)

print((g.number_of_edges() / g.number_of_nodes()**2) * 100)
```

## Possible visualization with Javascript... not so stable though, can be skipped.

    # https://andrewmellor.co.uk/blog/articles/2014/12/14/d3-networks/
    # https://github.com/brandomr/ner2sna
 
    # %%

    from IPython.display import HTML


    # %%

    get_ipython().run_cell_magic('HTML', '', "\n<iframe height=400px width=100% src='force.html'></iframe>")

# Planars graphs and maps :
Open Street Map interfaced with Networkx, using the package `osmnx`:
!!! Known bug:
https://stackoverflow.com/questions/59658167/cannot-import-name-crs-from-pyproj-for-using-the-osmnx-library
and
https://stackoverflow.com/questions/60312055/python-getting-typeerror-argument-of-type-crs-is-not-iterable-with-osmnx
so pick version 0.14 at least
```conda install osmnx>=0.14```
or
```pip install osmnx>=0.10```
For Windows users there might be some trouble with installing the
`fiona` package, see:
https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda
and
https://jingwen-z.github.io/how-to-install-python-module-fiona-on-windows-os/

# Special case for `osmnx` on `Windows` follow the next step in order:
* `pip install osmnx`
* `pip install Rtree`
* `conda install -c conda-forge libspatialindex=1.9.3`
* `pip install osmnx`
* Install all packages required up to `fiona`.
* `conda install -c conda-forge geopandas`
* say yes to everything
* Once done,  launch `pip install osmnx==1.0.1`
You will also need to install the package `folium`

```python
import folium
```

```python
map_osm = folium.Map(location=[43.610769, 3.876716])
```

```python
map_osm.add_child(folium.RegularPolygonMarker(location=[43.610769, 3.876716],
                  fill_color='#132b5e', radius=5))
map_osm
```


```python
import osmnx as ox
ox.utils.config(use_cache=True)  # caching large download
ox.__version__
```

```python
G = ox.graph_from_place('Montpellier, France', network_type='bike')
print(f"nb edges: {G.number_of_edges()}")
print(f"nb nodes: {G.number_of_nodes()}")
```

```python
ox.plot_graph(G)
```
# Visualize shorthest path between two points.
https://blog.ouseful.info/2018/06/29/working-with-openstreetmap-roads-data-using-osmnx/

```python
origin = ox.geocoder.geocode('Place Eugène Bataillon, Montpellier, France')
destination = ox.geocoder.geocode('Maison du Lez, Montpellier, France')

origin_node = ox.get_nearest_node(G, origin)
destination_node = ox.get_nearest_node(G, destination)

print(origin)
print(destination)
route = nx.shortest_path(G, origin_node, destination_node)
# XXX double check if weights are taken into account.
```


```python
ox.plot_graph_route(G, route)
```
```python
ox.plot_route_folium(G, route, weight=5, color='#AA1111', opacity=0.7)
# Adapted from : https://blog.ouseful.info/2018/06/29/working-with-openstreetmap-roads-data-using-osmnx/
```


```python
G.is_multigraph()
```

```python
edges = ox.graph_to_gdfs(G, nodes=False, edges=True)
nodes = ox.graph_to_gdfs(G, nodes=True, edges=False)
# Check columns
print(edges.columns)
print(nodes.columns)
```


```python
D = nx.incidence_matrix(G, oriented=True).T
```

```python
element = np.zeros(1, dtype=float)
mem = np.prod(D.shape) * element.data.nbytes / (1024**2)
print('Size of full matrix with zeros: {0:3.2f}  MB'.format(mem))

print('Size of sparse matrix: {0:3.2f}  MB'.format(D.data.nbytes/(1024**2) ))

print('Ratio  of full matrix size / sparse: {0:3.2f}%'.format(100 * D.data.nbytes / (1024**2 * mem)))
print(isspmatrix(D))
```python


**Alternatively**: you can uncomment the following line,
and check that the size of a similar matrix, with non-sparse
format would be.
```>>> Size of full matrix with zeros: 4 gB```

Creation a matrix of similar size. BEWARE CREATE HUGE MATRIX:

```python
M = np.random.randn(G.number_of_nodes(), G.number_of_nodes())
print('Size of full matrix with zeros: {0:3.2f}  MB'.format(M.nbytes/(1024**2)))
```


### Graph sparsity

```python
print(" {0:.2} % of edges only are needed to represent the graph of Montpellier".format(100 * G.number_of_edges() / G.number_of_nodes() ** 2))
```


To go further on the visualization of geographical graphs:
1. https://geoffboeing.com/2016/11/osmnx-python-street-networks/
2. https://automating-gis-processes.github.io/2017/lessons/L7/network-analysis.html
3. https://automating-gis-processes.github.io/2018/

```python
import geopandas
```


```python
df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
plt.show()
```
## For more on profiling
In Python `snakeviz` could help, see https://jiffyclub.github.io/snakeviz/
In R, `profvis` is equivalent, see https://rstudio.github.io/profvis/

## Debugging : package `pdb`
inspired by
https://davidhamann.de/2017/04/22/debugging-jupyter-notebooks/
Let us use
`import pdb; pdb.set_trace()`
to enter a code and inspect it.
Push the key `c` and then `enter` to go next.
See also:
https://www.codementor.io/stevek/advanced-python-debugging-with-pdb-g56gvmpfa.

A first recommendation is to use the Python debugger in your IDE.
For VScode: see for instance https://www.youtube.com/watch?v=w8QHoVam1-I


A possibility for pure Python or IPython is to use the `pdb` package and the
command `pdb.set_trace()`.
A command prompt launches when an error is met, and you can check the current
status of the environnement.
Useful shortcuts are available (e.g., touche c, touche j etc.) here:
https://docs.python.org/3/library/pdb.html)

```python
def function_debile(x):
    answer = 42
    answer += x
    return answer
```

```python
function_debile(12)
```

```python
def illustrate_pdb(x):
    answer = 42
    import pdb; pdb.set_trace()
    answer += x
    return answer
```

```python
illustrate_pdb(12)
```


`pdb`. A terminal is laucnhed when a problem occurs, and one can then take over and see what's going on.

```python
get_ipython().run_line_magic('pdb', '')
```

```python
def blobl_func(x):
    answer = 0
    for i in range(x, -1, -1):
        print(i)
        answer += 1 / i

    return answer

blobl_func(4)
```python
