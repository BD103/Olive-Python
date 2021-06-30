Creating a New Project
======================

Time for you to start a new project. Open up the console in whatever program / folder you use and run the following:

.. code-block:: console

   $ poetry init

   This command will guide you through creating your pyproject.toml config.

   Package name [example]:
   Version [0.1.0]:
   Description []:
   Author [None, n to skip]: Your Name <email@email.com>
   License []: MIT (We'll get to this later!)
   Compatible Python versions [^3.8]:

   Would you like to define your main dependencies interactively? (yes/no) [yes] no
   Would you like to define your development dependencies interactively? (yes/no) [yes] no

   [some]
   tomlcode = "here"

   Do you confirm generation? (yes/no) [yes]

This should give you a nice ``pyproject.toml`` file. This file contains all the configurable information about your project. Let's take a look.

.. code-block:: toml

   [tool.poetry]
   # name of pypi id and usually package folder
   name = "example"
   # not much to say here except use semver
   version = "0.1.0"
   # short text about your project
   description = ""
   # List of authors
   authors = ["Your Name <email@email.com>"]
   # Choose a license from https://python-poetry.org/docs/pyproject/#license
   license = "MIT"

   # installed when downloading the production package
   [tool.poetry.dependencies]
   python = "^3.8"

   # installed when running "poetry install"
   [tool.poetry.dev-dependencies]

   # don't touch this section
   [build-system]
   requires = ["poetry-core>=1.0.0"]
   build-backend = "poetry.core.masonry.api"

There's a lot to be said about this file. Thankfully, I'm going to stick to the `DRY <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_ philosophy and give you `a link to all the options <https://python-poetry.org/docs/pyproject/>`_ instead.

Now run:

.. code-block:: console

   $ poetry lock
   Updating dependencies
   Resolving dependencies... (0.1s)

   Writing lock file
   $ poetry install
   Installing dependencies from lock file

That's enough commands for now. Let's create some files::

  project/
  + example/
  | + __init__.py
  + README.md
  + pyproject.toml
  + poetry.lock

Move on to the next few sections to learn about dependency management and more.

.. todo:: Make more clear and less abrupt
