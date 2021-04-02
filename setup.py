#! /usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
  name = 'robotframework-nsm',
  packages = ['nsm'],
  version = '0.18',
  license='MIT',
  description = 'Robotframework library for NSM',
  long_description='''Robotframework-NSM
==================

.. contents::

Introduction
------------

Natural semantic metalanguage package for `Robot Framework`_
The package is based on works by prof. Anna Wierzbicka 
and prof. Cliff Goddard and this is work in progress.


Robotframework-NSM is operating system independent and supports Python 2.7 as well
as Python 3.x or newer. 

Documentation
-------------

For general information about using test libraries with Robot Framework, see
`Robot Framework User Guide`_.

Installation
------------

The recommended installation method is using pip_::

    pip install --upgrade robotframework-nsm

With recent versions of ``pip`` it is possible to install directly from the
GitHub_ repository. To install latest source from the master branch, use
this command::

    pip install git+https://github.com/AdamPrzybyla/robotframework-nsm.git

Alternatively you can download the source distribution from PyPI_, extract
it, and install it using one of the following depending are you using
Python or Jython::

    python setup.py install

Usage
-----

Sample test cases:

.. code:: robotframework

	Test 1
		Teraz jest tak: ja widze webpage
		Ja nie widze slowa logged na webpage
		Potem ja uzyje slow credentials na webpage
		Z tego powodu ja widze slowa logged na webpage
		Niedlugo potem ja nie widze webpage

	Test 2
		Teraz jest tak: ja widze webpage
		Ja nie widze slowa logged na webpage
		Potem ja uzyje slow bad credentials na webpage
		Z tego powodu ja nie widze slowa logged na webpage
		Niedlugo potem ja nie widze webpage

	Test 3
		Teraz jest tak: ja widze webpage
		Ja nie widze slowa logged na webpage
		Niedlugo potem ja nie widze webpage

Support
-------

If the provided documentation is not enough, there are various support forums
available:

- `robotframework-users`_ mailing list

.. _github: https://github.com/AdamPrzybyla/robotframework-nsm
.. _Robot Framework: http://robotframework.org
.. _Robot Framework User Guide: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-test-libraries
.. _PyPI: https://pypi.python.org/pypi/robotframework-nsm
.. _pip: http://pip-installer.org
.. _robotframework-users: http://groups.google.com/group/robotframework-users
''',
  author = 'Adam Przybyla',
  author_email = 'adam.przybyla@gmail.com',
  url = 'https://github.com/AdamPrzybyla/robotframework-nsm',
  download_url = 'https://github.com/AdamPrzybyla/robotframework-nsm/archive/v_18.tar.gz',
  keywords = ['robotframework', 'nsm', 'automatisation', 'tests'],
  install_requires=[
          'robotframework',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 2',
  ],
)
