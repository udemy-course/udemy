
from udemy import __title__
from udemy import __version__
from udemy import __author__
from udemy import __email__

# from distutils.core import setup
from setuptools import setup

setup(name=__title__,
      version=__version__,
      author=__author__,
      author_email=__email__,
      url='https://github.com/udemy-course/udemy',
      packages=['udemy'],
      install_requires=[
        'requests'
      ],
      entry_points='''
        [console_scripts]
        udemy-cli=udemy.cli:main
      ''',
)
