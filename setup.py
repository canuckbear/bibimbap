#
# The contents of this file are subject to the Apache 2.0 license you may not
# use this file except in compliance with the License.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
#
# Copyright 2017 SBIT project (http://www.firmwaretoolkit.org).
# All rights reserved. Use is subject to license terms.
#
#
# Contributors list :
#
#    William Bonnet     wllmbnnt@gmail.com, wbonnet@theitmakers.com
#

from mule.release import __version__, __author__, __author_email__

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bunch of Inexpensive Boards In order to Mimiic Brain AActivity Phenomena',
    'long_description': 'bibimbal is an artificial intelligence tool used to modelize brain activity when it',
    'comes to information storage retrieval and bas computation'
    'author': __author__,
    'url': 'https://github.com/canuckbear/bibimbap/',
    'download_url': 'https://github.com/canuckbrear/bibimbapmule/',
    'author_email': __author_email__,
    'version': __version__,
    'install_requires': [ 'pyyaml' ],
    'packages': ['sbit'],
    'scripts': [ 'bin/sbit' ],
    'name': 'sbit'
}

setup(**config)
