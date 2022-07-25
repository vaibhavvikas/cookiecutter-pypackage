# !/usr/bin/env python

from distutils.core import setup
from pathlib import Path

project_dir = Path(__file__).parent

setup(
    name='cookiecutter-pypackage',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a Python package',
    author='Vaibhav Vikas',
    license='BSD',
    author_email='vbhvvikas@gmail.com',
    url='https://github.com/vaibhavvikas/cookiecutter-pypackage',
    keywords=['cookiecutter', 'template', 'package', ],
    python_requires='>=3.8',
    install_requires=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
)
