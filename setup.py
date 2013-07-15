from setuptools import setup, find_packages

requires_list = [
  'argparse>=1.2.1',
  'colorama>=0.2.5',
  'coverage>=3.6',
  'mock>=1.0.1',
  'nose>=1.3.0',
  'rauth>=0.5.5',
  'requests>=1.2.3',
  'wsgiref>=0.1.2']

setup(name='buffpy',
      version='1.0b',
      platforms='any',
      description='Python library for Buffer App',
      author='Vlad Temian',
      author_email='vladtemian@gmail.com',
      url='https://github.com/vtemian/buffpy',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires_list,
     )
