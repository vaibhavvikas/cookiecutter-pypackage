## Cookiecutter PyPackage

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/vaibhavvikas/cookiecutter-pypackage/
* Free software: BSD license

## Features

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Docs using github pages and Minimalistic theme
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/vaibhavvikas/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements.txt``)
* Register_ your project with PyPI.
* Go to your project settings and activate GitHub pages and specifiy the docs folder for the documentations to be published at your github pages website.
* Release your package by pushing a new tag to main.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
