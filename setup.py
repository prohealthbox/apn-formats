import apn
from setuptools import setup, find_packages

install_requires = [
      "fuzzywuzzy >= 0.15.0",
      "python-Levenshtein >= 0.12.0",
]

setup(name=apn.__title__,
      version=apn.__version__,
      description=apn.__summary__,
      long_description=open("README.rst").read(),
      license=apn.__license__,
      url=apn.__uri__,

      author=apn.__author__,
      author_email=apn.__email__,
      packages=["apn"],
      package_data={'apn': ['*.pkl']},
      )
