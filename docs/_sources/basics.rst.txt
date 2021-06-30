The Basics
==========

In Python you can import code from another module (``.py`` file).

>>> from scripts import shout
>>> shout("Hello, world!")
HELLO, WORLD!

This allows you to clean up your main file and organize your program. This method is called modularized code. There is also another way to modularize, which takes after the first method but expands it.

Python packages. They allow you to *organize* your code even more through folders::

  project/
  + main.py
  + package/
  | + __init__.py
  | + submodule1.py
  + module1.py

This is an example of a program containing a package. All a package needs is a folder and a file called ``__init__.py`` inside. Try putting some code inside this file then importing the package.

The Quirkiness of ``__init__.py``
---------------------------------

When I first started making packages, ``__init__.py`` confused me. Let me try to explain how it works.

We have a folder named ``vehicles``. Inside we have three empty files:

* ``__init__.py``
* ``car.py``
* ``bike.py``

>>> import vehicles
>>> type(vehicles)
<class 'module'>
>>> type(vehicles.car)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'vehicles' has no attribute 'car'

We learn two things from this example. First: Python does not separate packages and modules. They are of the same type. Second: modules inside of a package are not automatically imported when you import the package.

What does this mean?

  When you import a package, you are really importing the ``__init__.py`` file. Therefor, if you import in ``__init__.py``, it will become global to the package.

Let's change the contents of ``car.py``:

.. code-block:: python

   # car.py

   class Car(object):
     def __init__(self, color):
       self.color = color

Now let's run some tests:

>>> from vehicles import car
>>> x = car.Car("blue")
>>> type(x)
<class 'vehicles.car.Car'>

Now notice if we run another test.

>>> import vehicles
>>> x = vehicles.car.Car("blue")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'vehicles' has no attribute 'car'

What do we learn here? You can import modules directly from a package, but it still doesn't automatically import them.

Now, let's try this. Write the following to ``__init__.py``:

.. code-block:: python

   from .car import Car

>>> import vehicles
>>> x = vehicles.Car("blue")
>>> type(x)
<class 'vehicles.car.Car'>

It worked! In summary:

* When importing a package, you really are importing the ``__init__.py`` file
* This file should import all the bits and bobs of other files with a relative import command (a dot before the name)
* Take `Flask's <https://github.com/pallets/flask/blob/main/src/flask/__init__.py>`_ ``__init__.py`` file. It imports many classes and functions from different modules, but only has one variable.
* If you don't have enough functions to modularize, or don't believe that it is necessary, read our pymodule page.

.. todo:: Add pymodule page

Learn from Others
-----------------

Sometimes an explanation is too vague or isn't covered at all. If this is the case, there are many things to do:

* Search it up on the internet

  * `Google <https://google.com>`_ is extremely helpful and can solve your question most of the time

* Ask the question in a coding-based forum

  * I find that the `Replit Talk <https://replit.com/talk/all>`_ community can be very helpful
  * `Stack Overflow <https://stackoverflow.com/>`_ is also great

* Open an issue on the `Olive Python Github <https://github.com/BD103/Olive-Python/issues>`_

  * I will try to answer as quickly as possible, and I might add the solution to this guide as well!
