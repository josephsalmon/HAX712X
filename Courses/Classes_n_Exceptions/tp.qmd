# Classes and exceptions

## Classes (to be investigated more later on)

 * *classes* are central elements in *Object-oriented programming (OOP)*

 * Class: structure that represent an object, its properties, and all the operations one can apply to it.

In Python a class contains *attributes* (variables) and *methods* (functions).
It is defined similarly to a function, with replacing the `def` keyword by `class`. The name of a class should be CapWords or CamelCase (the naming coming from the "bumpy" look of its letters); see examples below.

Usually a class contains some class methods (functions inside the class).

* The first argument of a (non `static`) method is usually called `self`:  it is a mandatory element. This `self` argument is for self reference.

* Some method names have a specific meaning, for instance:
   * `__init__`:  name of the method invoked when creating the object (instantiation)
   * `__call__`: method invoked when calling the object
   * `__str__` : method invoked when a class has a representation as a string, e.g., for when passing it to the `print` function
   * see <http://docs.python.org/3/reference/datamodel.html#special-method-names> for more special names.

### Example

Let us define a simple object:

```python
class Point(object):
    """A class to represent planar points."""

    def __init__(self, x, y):
        """Create a new point (x, y)."""
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """Translate the point by dx and dy."""
        self.x += dx
        self.y += dy

    def __str__(self):
        return "Point: [{0:1.3f}, {1:1.3f}]".format(self.x, self.y)
```

Remark: if you are not familiar with printing in Python, start with the new f-strings format, see for instance: <https://zetcode.com/python/fstring/>


To create a new instance of the class `Point`:

```python
p1 = Point(x=0, y=0)  # call __init__ ;
print(p1.x)
print(p1.y)
print("{0}".format(p1))  # call __str__
p1
```

To apply the translate method:

```python
p1.translate(dx=1, dy=1)
print(p1.translate)
print(p1)
print(type(p1))
```

To run a method of the object `p1` (which is an instance of `Point`) simply use the dot notation: p1.translate(arg1, arg2)


```python
p2 = Point(1, 1)
p1.translate(0.25, 1.5)
print(p1)
print(p2)
```
Remark: you might have already used that dot notation with `numpy` for instance when executing numpy functions as follows


```python
import numpy as np
rng = np.random.default_rng(seed=12345)
a = rng.random((3, 3))
a.mean(axis=0)
```

About `__call__`: `MyClass(arg1, arg2, ...)` is a shorthand for `MyClass.__call__(arg1, arg2, ...)`, so this allows to to write classes where the instances behave like functions and can be called like a function

```python
class Sum:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a + b)

# Instance created
sum_as_a_function = Sum()

# __call__ method will be called
sum_as_a_function(10, 20)
```
Test function of interest: `isinstance` allow to check if an object is of the correct class.
```python
isinstance(sum_as_a_function, Sum)
isinstance(sum_as_a_function, Point)

```


### Remarks

 * A method of a class is able to modify the state of a particular instance.
 This does not alter the other instantiations of the class.
 * Methods that do not depend on a particular instantiation can be decorated with the `@staticmethod` keyword. Such method **do not** have their first arg referring to `self`...

---
### <font color='red'>Exercise : Gaussian class </font>


Implement a class `Gaussian` with attributes `mean` and `std` with a method
- `__str__` returning a string with the expression of the density
- `__eq__`  testing the equality of two instances. You should use numpy.isclose()
- `__add__` implementing the addition of independent Gaussian, or more precisely their pdfs (probability density functions)
- `__radd__` implementing the addition of independent Gaussian, or more precisely their pdfs (probability density functions)

Note: when executing `a+b` what really happens is that the __add__ method of the `a` object is called `a.__add__(b)`


```python
class Gaussian:
    # XXX TODO

g1 = Gaussian(0.0, 1.0)
g2 = Gaussian(1.0, 2.0)
g3 = Gaussian(2.0, 2.0)
g4 = Gaussian(3.0, 3.0)

print(g1)
print(g2)
print(g3)
print(g4)
print(g2 + g1)
print(sum([g1, g2, g3]))
print(sum([g1, g2, g3]) == g4)

# # The former should display
# # The density function is: exp(-(x - 0)^2 / (2*1^2)) / sqrt(2 * pi * 1^2)
# # The density function is: exp(-(x - 1)^2 / (2*2^2)) / sqrt(2 * pi * 2^2)
# # True
# # False
# # The density function is: exp(-(x - 1)^2 / (2 * 2.23606797749979^2)) / sqrt(2 * pi * 2.23606797749979^2)
```
---

### Inheritance, the sub-Gaussian case (of a kind)

Classes can inherit methods from other classes. You can use `super` (latin for "above") to access to the parent class.

Test function of interest: `isinstance` allow to check if an object is of the correct class.

```python
class IsoGaussian(Gaussian):
    def __init__(self, mean):
        super().__init__(mean, 1.0)

gg1 = IsoGaussian(3)
print(gg1)
issubclass(IsoGaussian, Gaussian)

```

Example of interest: https://github.com/scikit-learn/scikit-learn/blob/95119c13a/sklearn/linear_model/_base.py#L391

More info on `super`: https://realpython.com/python-super/

## Exceptions

Sources: see https://fabienmaussion.info/scipro_ss2018/html/09-Exceptions.html
 * In Python errors are handled through `Exceptions`
 * An error throw an `Exception` interrupting the normal code execution
 * Execution can overpass such an issue inside a bloc with `try` - `except`


* A typical use case: stop the program when an error occurs:

```python
def my_function(arguments):

    if not verify(arguments):
        raise Exception("Invalid arguments")

    # keep continuing
```

The list of possible errors is available here:
One may use `try`, `except`, `finally` to prevent errors to stop the program:
https://docs.python.org/3/library/exceptions.html#bltin-exceptions
and includes: NameError, ImportError, AssertionError etc.

```python
try:
    # normal code 1 goes here
except:
    # code for error handling goes here
    # this code 2 is not executed unless the code 1
    # above generated an error
finally:
    # optional. This clause is executed no matter what,
    # and is generally used to release external resources.
```

### Example


```python
try:
    print("test_var")
    e = 4
    print(test_var) # raise an error: the test_var variable is not defined
except NameError:
    print("Caught an exception: test_var does not exist")
finally:
    print("This code is executed every time")

print("The program keep continuing... it does not freeze!")
print('Beware! the variable ', 'e =', e, 'is still defined.')
```

To obtain some information on the error: it is possible to access the instance of the `Exception` class thrown by the program through the syntax:


```python
try:
    print("test")
    print(testtt)  # error: the variable testtt is not defined
except Exception as e:
    print("Caught an exception:", e)
```

**Note** a common use case is to test if the import of a package was successful or not

```python
try:
    import ddownload
except Exception as e:
    print(e)
```

Other common exceptions: <https://docs.python.org/3/library/exceptions.html>

### The `with` statement

**Warning**: you have to run the following lines with a directory `scripts/` containing a function `hello-world.py`

```python
fname = "scripts/hello-world.py"

with open(fname) as file:  # Use file to refer to the file object
    data = file.read()
    print(data)
    # at the end of the code chunk, the file.__exit__() method is called (i.e., file.close() is done automatically)
```

Now

```python
fname = "scripts/hello-world_do_not_exist.py"
try:
    # 1/0  # uncomment at some point and run
    file = open(fname)
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
except (RuntimeError, TypeError, NameError, ZeroDivisionError):
    print("Specific Error message 2")
finally:
    file.close()  # important to release the access to the file !
```

---
### <font color='red'>Exercise : Improving the Gaussian class</font>

Create a sub-class `GaussianBis` where you check if the user has provided float arguments (see also `assert` and `isinstance` routines).
Print a custom explicit error message if it is not the case.

```python
class GaussianBis:
    # XXX TODO
```
---


## Scope

```python
e = 0
print(e)

for i in range(1):
    e = 1

print(e)


def f():
    e = 2

print(e)
```

**Conclusion**: `e` is only "visible" inside the function definition.
See https://realpython.com/python-scope-legb-rule/ for more information on this topics.


## Manipulate file names on disk across platforms.

The following would avoid naming conflict due to each OS (Linux / Windows /Mac) syntax. This is important for your project if you work with colleagues having a different OS than yours!!!


```python
import os
#
print(os.path.join('~', 'work', 'src'))
print(os.path.join(os.getcwd(), 'new_directory'))
os.path.expanduser?
print(os.path.expanduser(os.path.join('~', 'work', 'src')))
```

---
### <font color='red'>Exercise : Create a bunch of files</font>

Write a simple script that creates, in the sub-directory `scripts`, the following text files: `myDb_000.txt`, `myDb_001.txt`, `myDb_002.txt`, ..., `myDb_049.txt`. The `i`-th file should contains a single line with the average of the `i` first digits of pi.


**Hint**:
- you might need zero padding
- you can check what the following code does

```python
file = open("copy.txt")
file.write("Your text goes here")
file.close()
```
- you might also need some precision for the digits of $\pi$, hence using `mpmath` instead of `numpy`

```python
from mpmath import mp
import numpy as np

if not os.path.isdir("script"):
    os.mkdir("script")

for i in range(2, 50):


for i in range(2, n_tot + 2):
    val = '0' + str(i)
    print(str(f"{i:{val}}"))
```

```python
import os
import math

# XXX TODO
```

## More links

* http://www.python.org - Python official web page
* http://www.python.org/dev/peps/pep-0008 - Style and writing recommendation
* http://www.greenteapress.com/thinkpython/ - A free book on python
* [Python Essential Reference](http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786) - a good reference for general Python coding
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) - an excellent book for data science in Python
