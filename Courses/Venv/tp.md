# Virtual Python Environment

## Preamble

A venv is an isolated standalone python distribution with specific version of modules. This is useful when one need to run different python versions in a single system. There are various commands that are able to create a venv: `venv`, `virtualenv`, `conda`... We are going to use `Anaconda` to set up various `python` virtual environments on our system. 

More information are available at: <https://virtualenv.pypa.io/en/latest/>, <https://docs.python.org/3/library/venv.html>

## Python package system

The Python Package Index (PyPI) is a repository of software for the Python programming language.  PyPI helps you find and install software developed and shared by the Python community.

The `pip` program allows you to install.

```bash
$ pip --version
$ pip install numpy
```

Please have a look to <https://pypi.org/>, <https://packaging.python.org/tutorials/installing-packages/> to solve the following 

----
### <font color='red'>Exercise:</font>

1. Determine which python version there is on your system using `locate` and `which`
2. Determine which version of python is used by the `pip` command
3. List all the python modules installed with the `pip` command
----

## Anaconda

Anaconda is a package manager, an environment manager coming with a Python/R data science distribution, and a large collection of open-source packages. It is cross-platform and is a very popular choice in the data scientist community. Nevertheless, it suffers from a main drawback: it is heavy. Moreover, it comes with its own package manager `conda` which allows you to install python module (like `pip`) and other programs. 

On the Linux box provided by the FdS, there is a terminal with the $PATH environment variable already configured (`/net/apps/bin/init_anaconda3`). You may launch it via the Graphical User Interface.

----
### <font color='red'>Exercise:</font>

1. Display the $PATH variable in the `Anaconda_init` terminal
2. Type `conda deactivate` and (re)-display the $PATH variable
----

### Creating an environment

Use the terminal or an Anaconda Prompt for the following steps:

1. To create an environment:

    ```bash
    $ conda create --name myenv
    ```

    Replace ``myenv`` with the environment name.

2. When conda asks you to proceed, type ``y``:

    ```bash
      proceed ([y]/n)?
    ```

    By default, environments are installed into the `envs` sub-directory in your `conda` directory. See `conda create --help` for information on specifying a different path. This creates the `myenv` environment in ``envs/``. This environment uses the same version of Python that you are currently using because you did not specify a version.

3. To create an environment with a specific version of Python:

    ```bash
    $ conda create -n myenv python=3.6
    ```

4. To create an environment with a specific package:

    ```bash
    $ conda create -n myenv scipy
    ```

   or:

    ```bash
    $ conda create -n myenv python
    $ conda install -n myenv scipy
    ```

5. To create an environment with a specific version of a package:

    ```bash
    $ conda create -n myenv scipy=0.15.0
    ```
   
    or

    ```bash
    $ conda create -n myenv python
    $ conda install -n myenv scipy=0.15.0
    ```

6. To create an environment with a specific version of Python and multiple packages:

    ```bash
    $ conda create -n myenv python=3.6 scipy=0.15.0 astroid babel
    ```

See: <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands>

----
### <font color='red'>Exercise:</font>

1. Create a new environment called `toto` with `python3.5` and `pandas` version 0.23
2. Create another environment called `tata` with `python3.7` and `pandas` version 1.0
----

### Switch environment

To switch to an environment, it must be "activated" (in git we would have said "to checkout"). Activation entails two primary functions: adding entries to PATH for the environment and running any activation scripts that the environment may contain. These activation scripts are how packages can set arbitrary environment variables that may be necessary for their operation. You can also use the config API to set environment variables. To activate an environment: 

```bash
$ conda activate myenv
```

Change `myenv` with the name on your environment.

See: <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>

----
### <font color='red'>Exercise:</font>

1. Activate the `toto` environment. Launch `python` and check the version of `pandas`
2. Activate the `tata` environment. Launch `python` and check the version of `pandas`
3. List all the available environment (look in the documentation by yourself)
4. Come back to the `base` environment
----

### Save and export an environment

Have a look at <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments> and do the following

----
### <font color='red'>Exercise:</font>

1. Imagine that you are coding a python module and a user is not able to run your code due to some missing dependencies. How can you help him to set up his python venv?
----

### Remove environment and clean

Anaconda is particularly greedy in term of disk usage. It can be a good practice to remove an unused environment 

```bash
$ conda env remove -n myenv
```

To remove all cache and package run

```bash
$ conda clean --all
```

----
### <font color='red'>Exercise:</font>

1. Remove **all** the environments created during this session
2. Create an environment called `hmma238_env` with `matplotlib` (this venv will be used in the next courses)
3. Clean the `conda` caches to free disk space.
----