#!/usr/bin/env python
#Copyright (C) 2013 - The MITRE Corporation
#For license information, see the LICENSE.txt file
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info <(2, 6):
    raise Exception('libtaxii requires Python 2.6 or higher.')

install_requires = ['lxml>=2.3.2', 'M2Crypto>=0.21.1']

setup(name='libtaxii',
      description='TAXII Library.',
      author='Mark Davidson',
      author_email='mdavidson@mitre.org',
      url="http://taxii.mitre.org/",
      version='0.1',
      py_modules=['libtaxii.taxii_client', 'libtaxii.taxii_message_converter'],
      install_requires=install_requires,
      data_files=[('xsd', ['xsd/TAXII_XML_10.xsd',
                           'xsd/xmldsig-core-schema.xsd'])],
      long_description=open("README").read(),
      keywords="taxii libtaxii",
      )