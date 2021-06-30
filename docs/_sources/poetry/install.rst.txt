Installation
============

.. note:: 
   You don't need to follow this page if your are using `Replit <https://replit.com>`_

Requirements
------------

For the latest version (as of writing this), 1.1, you will need:

* Python 3.6 or greater (You technically can also use 2.7 or 3.5, but support is discontinued in the release of 1.2)

Install
-------

Now open up your console and run the following:

.. code-block:: console

   $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

If you are Windows, run this instead:

.. code-block:: powershell

   (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

You should now have Poetry installed. Test your version with:

.. code-block:: console

   $ poetry --version
   Poetry version 1.1.6

Alternative Methods (Not Recommended)
-------------------------------------

If you can't use a request, try one of these instead.

Method 1
~~~~~~~~

Download the `get Poetry script <https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py>`_ and then run it.

.. code-block:: console

   $ python get-poetry.py

Method 2
~~~~~~~~

Install it with PIP.

.. code-block:: console

   $ python -m pip install poetry

This is undesireable because then all of Poetry's dependencies are global. This may cause conflicts with your program. Poetry is meant to help you run environments, it doesn't want to interfere.
