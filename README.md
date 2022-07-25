## Cookiecutter PyPackage

Cookiecutter template for a Python package.

* GitHub repo: https://github.com/vaibhavvikas/cookiecutter-pypackage/
* Free software: BSD license

## Features

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Docs using github pages and Minimalistic theme
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

*Cookiecutter: https://github.com/cookiecutter/cookiecutter*

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

Generate a Python package project:

    cookiecutter https://github.com/vaibhavvikas/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Install the requirements into a virtualenv. (``pip install -r requirements.txt``)
* Register your project with PyPI.
* Go to your project settings and activate GitHub pages and specifiy the docs folder for the documentations to be published at your github pages website.
* Release your package by pushing a new tag to main.
* In the ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`.

pip docs for requirements files: https://pip.pypa.io/en/stable/user_guide/#requirements-files

Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives


## Setting up Github pages:

* Go to repository settings and navigate to github pages from the sidebar.
* In the source dropdown, select your default branch where you have the docs folder.
* In the folder dropdown selct `\docs`.
* Click on `save`. The github action for github pages deployment will start after that you can check the github pages when its complete.

## Known Issues:

Github Pages don't support the files or links of files outside the github pages folder i.e. you can't access files in the parent directory. As a result you'll need to copy the contents of the corresponding files from your main repo to the files inside docs folder. I know its kind of redundant. I will update if I find any solution. Suggestions are welcome (:
