# Creating a `python` module

## What is a `python` module?

You already know it: this is a set of `python` functions and statements, and this is what you import at the beginning of your `python` functions.

### A module could be a single file

Indeed, a module can simply be a single file:

```python
>>> import fibo
```

This does not enter the names of the functions defined in `fibo` directly in the current symbol table though; it only enters the module name `fibo` there.
Using the module name you can access the functions:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
>>> fibo.__file__
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

When importing a module, several methods are (automatically) defined.
Their names are usually prefixed and suffixed by the symbol `__`, e.g.,

```python
>>> fibo.__name__
'fibo'
>>> fibo.__file__
'/home/.../HAX712X/Courses/Python-modules/fibo.py'
```

### ... or a module could be a directory

You can also import a full directory (containing many `python` files stored in sub-folder). Python looks for a folder located in `sys.path` list. 
You have already imported the `numpy` module, for numerical analysis with `python`:

```python
>>> import numpy as np
>>> np.array([0, 1, 2, 3]).reshape(2, 2)
array([[0, 1],
       [2, 3]])
>>> np.array([0, 1, 2, 3]).mean()
1.5
```

In fact, you have imported the following folder:

```python
>>> np.__path__
['/usr/lib/python3.9/site-packages/numpy']
```
or possibly if you used anaconda to install `python`:
```python
>>> np.__path__
['/home/username/anaconda3/lib/python3.7/site-packages/numpy']
```

More precisely **this** file

```python
>>> np.__file__
'/usr/lib/python3.9/site-packages/numpy/__init__.py'
```

or

```python
>>> np.__file__
['/home/username/anaconda3/lib/python3.7/site-packages/numpy/__init__.py']
```


Any (sub-)directory of your python module should contain an `__init__.py` file!

**Useful tips:**

- The `__init__.py` file can contain a list of function to be loaded when the module is imported.
It allows to expose functions to user in a concise way.

- You can also import modules with relative path, using `.`, `..`, `...`, etc.
See: <https://realpython.com/absolute-vs-relative-python-imports/>

### The `dir()` function

The built-in function `dir()` is used to find out which names a module defines.
It returns a sorted list of strings:

```python
>>> import fibo, numpy
>>> dir(fibo)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
>>> fibo.__dir__
<built-in function __dir__>
>>> dir(numpy)
['ALLOW_THREADS',...,'zeros_like']
>>> numpy.__dir__
<function __dir__ at 0x7fe0a25e81e0>
```
The `0x7fe0a25e81e0` hexadecimal number is the `id` of the object:

```python
>>> hex(id(numpy.__dir__))
0x7fe0a25e81e0
```
This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value. (Implementation note: this is the address of the object.). See <https://docs.python.org/3/library/functions.html#id>

To list every element in your symbol table simply call `dir()`.

Reference: <https://docs.python.org/3/tutorial/modules.html#the-dir-function>

### Namespaces

A namespace is a set of names (functions, variables, etc.).
Different namespaces can co-exist at a given time but are completely isolated. In this way you can control which function you are using.

A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

```python
>>> cos(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cos' is not defined
>>> import math, numpy as np
>>> math.cos(3)
-0.9899924966004454
>>> np.cos(3)
-0.9899924966004454
```

References: <https://www.programiz.com/python-programming/namespace>

### The Module Search Path

When a module named `spam` is imported, the interpreter first searches for a built-in module with that name.
If not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`. The variable `sys.path` is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).

- The environment variable `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).

Reference: <https://docs.python.org/3/tutorial/modules.html#the-module-search-path>

### Checking if a module exists

Find the loader for a module, optionally within the specified path.

```python
>>> import importlib
>>> spam_spec = importlib.util.find_spec("spam")
>>> found = spam_spec is not None
>>> found
False
```
Now 

```python
>>> import numpy
>>> numpy_spec = importlib.util.find_spec("numpy")
>>> numpy_spec
ModuleSpec(name='numpy', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fe6bd502460>, origin='/usr/lib/python3.9/site-packages/numpy/__init__.py', submodule_search_locations=['/usr/lib/python3.9/site-packages/numpy'])
```
should return more information and where the loader is.


See <https://docs.python.org/3/library/importlib.html#importlib.find_loader> an <https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it>

### Lazy import

A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module.
They are executed only the **first time** the module name is encountered in an `import` statement.

To force a module to be reloaded, you can use `importlib.reload()`.

See: <https://docs.python.org/3/library/importlib.html#importlib.reload>

Remark: when using `ipython` (interactive `python`, an ancestor of the `jupyter notebook`), one can use the "magic" command
`%autoreload 2`, cf. <https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html?highlight=autoreload>

### "Compiled" `python` files

To speed up loading modules, `python` caches the compiled version of each module in the  `__pycache__` directory under the name `module.version.pyc`, where the version encodes the format of the compiled file; it generally contains the `python` version number. 

For example, in `CPython` release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`.
This naming convention allows compiled modules from different releases and different versions of `python` to coexist.

**Useful git tip:**

- you should add `__pycache__` entry in your `.gitignore` file to avoid to add compiled `python` file to your project.

## The Python Package Index (Pypi) repository

The `python` Package Index, abbreviated as PyPI, is the official third-party software repository for `python`.
PyPI primarily hosts `python` packages in the form of archives called `sdists` (source distributions) or pre-compiled "wheels".

----
### <font color='red'>Exercise:</font>

1. Go to <https://test.pypi.org/> and describe the aim of this repository.

### Pip

`pip` is a *de facto* standard package-management system used to install and manage software packages from PyPi.

```bash
$ pip install some-package-name
$ pip uninstall some-package-name
$ pip search some-package-name
```

----

----
### <font color='red'>Exercise : Create a bunch of files</font>


  1. Install the modules `download`, `setuptools`, `pandas`, `pygal` and `pygal_maps_fr`. Beware, you should use the option `--user` to force the installation in your home directory.
  2. List all the package in your venv using pip.

----

It is possible to install a **local** module with pip

```bash
$ pip install /path/to/my/local/module
```

where `/path/to/my/local/module` is the path to the module.
But if some changes occur in the `/path/to/my/local/module` folder, the module will not be reloaded.
This might be annoying during the development stage.
To force `python` to reload the module at each change call, consider the `-e` option:

```bash
$ pip install -e /path/to/my/local/module
```

## Creating a `python` module

References: <https://python-packaging.readthedocs.io/en/latest/>

### Picking A Name

Python module/package names should generally follow the following constraints:

- All lowercase
- Unique on PyPI, even if you do not want to make your package publicly available (you might want to specify it privately as a dependency later)
- Underscore-separated or no word separators at all, and do not use hyphens (i.e., use _ not -).

We are going to create a module called `biketrauma` to visualize the `bicycle_db` used in the the following lectures that can be found at <https://koumoul.com/s/data-fair/api/v1/datasets/accidents-velos/raw>.


### Module structure

The initial directory structure for `biketrauma` should look like this:

```bash
packaging_tutorial/
    biketrauma/
        __init__.py
        data/
    setup.py
    .gitignore
```

The top level directory is the root of our Version Control System (e.g. git) repository `packaging_tutorial.git`. The sub-directory, `biketrauma`, is the actual Python module.

---
### <font color='red'>Exercise : Create a bunch of files</font>

 We are going to create a new `python` module that can be used to visualize the bike dataset.

  1. Create a new folder `~/packaging_tutorial/` and initialize a git in it.
  2. Create a `.gitignore` file to ignore `__pycache__`, `.vscode` directories and files containing the string `egg-info` or `dist` in their name as well.
  3. Push your work into a new repository on your github.
  5. Create a sub-folder `~/packaging_tutorial/biketrauma`. This is where our `python` module will be stored.
  6. Create a `~/packaging_tutorial/biketrauma/__init__.py` file where a string `__version__` defined at `0.0.1`.
  4. Create an empty sub-folder `~/packaging_tutorial/biketrauma/data` locally on your computer/session.
  How to add it to git?  (Hint: `.gitkeep`)
  7. Create **an empty** `~/packaging_tutorial/setup.py` file.
  8. Commit and push into your repository.

Read also: <https://packaging.python.org/guides/single-sourcing-package-version/>.

---

### Sub-modules

The final directory structure of our module will look like:

```bash
  packaging_tutorial/
      biketrauma/
          __init__.py
          io/
            __init__.py
          preprocess/
            __init__.py
          vis/
            __init__.py
          data/
      setup.py
      script.py
```

----
### <font color='red'>Exercise : Create a bunch of files</font>

Add some `python` files in the `modules_files` folder:

  1. Add some sub-folders to `biketrauma` called `io` (for input/output), `preprocess`, `vis` (for visualization). Copy the `script.py` into the root folder.
  2. Populate the `preprocess` sub-module with the `get_accident.py` file (see the git repo of the course in the subfolder `Courses/Python-modules/modules_files`)
  3. Populate the `vis` sub-module with the `plot_location.py` file
  4. Populate the `io` sub-module with the file `Load_db.py` (it downloads the bike data-set). At the loading step your sub-module should create the variables
```python
url_db = "https://koumoul.com/s/data-fair/api/v1/datasets/accidents-velos/raw"
path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bicycle_db.csv")
```
----

### Adding additional files

In order to load the functions in the `io`, `preprocess` and `vis` sub-modules, you can add the following lines to the `~/packaging_tutorial/biketrauma/__init__.py`:

```python
from .io.Load_db import Load_db
from .vis.plot_location import plot_location
from .preprocess.get_accident import get_accident
```

----
### <font color='red'>Exercise : Create a bunch of files</font>

  1. Check that your module does work by launching the `script.py` script
  2. Create a file `format_date.py` in the `biketrauma.preprocess` module in which a function `format_date` format the date of the data-set in international format.
  3. This function should accessible with the command:

```python
import biketrauma

df = biketrauma.Load_db().save_as_df()
df_nicely_formated = biketrauma.format_date(df)
```
---

### Package the module with `setuptools`

The main setup configuration file, `setup.py`, should contain a single call to `setuptools.setup()`, like so:

```python
from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/xxxxxxxxxxx.git',
  author='xxxxxxxxxxx',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)
```

To create a `sdist` package (a source distribution):

```bash
$ cd ~/packaging_tutorial/
$ python setup.py sdist
```

This will create `dist/biketrauma-0.0.1.tar.gz` inside the top-level directory. You can now install it with

```bash
$ pip install ~/packaging_tutorial/dist/biketrauma-0.0.1.tar.gz
```

See <https://setuptools.readthedocs.io/en/latest/setuptools.html> and <https://packaging.python.org/tutorials/packaging-projects/>

### Add requirement file

To get a list of the installed package in your current venv, you can use the following command:

```bash
$ pip freeze > requirements.txt
```
Unfortunately, it may generate a way too large collection of packages dependencies. To get a sparser list, you can use `pipreqs`

---
### <font color='red'>Exercise : Create a bunch of files</font>


1. Create a minimal `requirements.txt` file with `pipreqs`. Add it to the `biketrauma` module.

---

### Upload on PyPI

`twine` is a utility for publishing Python packages on PyPI. We are going to use the test repository <https://test.pypi.org/>.

---
### <font color='red'>Exercise : Create a bunch of files</font>


  1. Create an account on the PyPI test repository

This is quite easy to upload a python module on PyPI:

1. Create some distributions in the normal way:

```bash
$ python setup.py sdist bdist_wheel
```

2. Upload with twine to Test PyPI and verify things look right.
Twine will automatically prompt for your username and password:

```bash
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
username: ...
password: ...
```

3. Upload to PyPI:

```bash
$ twine upload dist/*
```
---

More documentation on using `twine` to upload packages to PyPI is in the [Python Packaging User Guide](https://packaging.python.org/tutorials/distributing-packages/https://packaging.python.org/tutorials/distributing-packages/).

References: <https://pypi.org/project/twine/>
