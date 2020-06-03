#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-template-check',
    version='0.3.1',
    description='Perform (minimal) syntax checks for Django templates.',
    long_description="\n".join([open('README.rst').read(),
                                open('CHANGES.rst').read()]),
    url='https://github.com/joostrijneveld/django-template-check',
    author='Joost Rijneveld',
    author_email='joost@joostrijneveld.nl',
    license='CC0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='django templates syntax check',
    packages=find_packages(),
    install_requires=['django>=1.8'],
)
