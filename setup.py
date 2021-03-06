#!/usr/bin/env python

from setuptools import setup

setup(
    name='git-search-replace',
    version='1.0.2',
    author='Dan Aloni',
    author_email='alonid@gmail.com',
    packages=['gitsearchreplace',],
    url='https://github.com/da-x/git-search-replace',
    license='LICENSE.txt',
    description='a utility on top of git for project-wide '
                'search-and-replace that includes filenames too',
    long_description=open('README.md').read(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points = {
        'console_scripts': [
            'git-search-replace.py = gitsearchreplace:main',
        ]
    }
)
