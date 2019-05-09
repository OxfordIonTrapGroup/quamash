from setuptools import setup

import re
import os.path

__author__ = 'Mark Harviston <mark.harviston@gmail.com>, Arve Knudsen <arve.knudsen@gmail.com>'
__version__ = '0.6.1'
__url__ = 'https://github.com/harvimt/quamash'
__license__ = 'BSD'
__all__ = ['QEventLoop', 'QThreadExecutor']

groups = re.findall(r'(.+?) <(.+?)>(?:,\s*)?', __author__)
authors = [x[0].strip() for x in groups]
emails = [x[1].strip() for x in groups]

desc_path = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(desc_path, encoding='utf8') as desc_file:
	long_description = desc_file.read()

setup(
	name='Quamash',
	version=__version__,
	url=__url__,
	author=', '.join(authors),
	author_email=', '.join(emails),
	packages=['quamash'],
	license=__license__,
	description=__doc__,
	long_description=long_description,
	keywords=['Qt', 'asyncio'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: BSD License',
		'Intended Audience :: Developers',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3 :: Only',
		'Environment :: X11 Applications :: Qt',
	],
	# FIXME depends on PyQt4, PyQt5 or PySide, but cannot put that in a setup.py
	extras_require={
		'test': ['pytest'],
	},
)
