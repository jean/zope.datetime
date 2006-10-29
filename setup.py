##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.datetime package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension

setup(name='zope.datetime',
      version='3.4-dev',
      url='http://svn.zope.org/zope.datetime',
      license='ZPL 2.1',
      description='Zope datetime',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="Commonly used date and time related utility functions.",

      packages=['zope',
                'zope.datetime',
                'zope.datetime.tests'],
      package_dir = {'': 'src'},

      namespace_packages=['zope',],
      tests_require = ['zope.testing'],
      install_requires=[],
      include_package_data = True,

      zip_safe = False,
      )
