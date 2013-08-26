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
      version='1.03b',
      platforms='any',
      description='Python library for Buffer App',
      author='Vlad Temian',
      author_email='vladtemian@gmail.com',
      url='https://github.com/vtemian/buffpy',
      packages = ['buffpy'],
      include_package_data=True,
      install_requires=requires_list,
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
      ]
     )
