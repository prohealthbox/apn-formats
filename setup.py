from setuptools import setup, find_packages

setup(name='apn',
      version='1.0',
      description='APN format verification tool',
      author='Eric Proulx and Ken Harmon',
      packages=find_packages(),
      package_data={'apn': ['*.pkl']},
      )
