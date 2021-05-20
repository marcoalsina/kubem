import os
from setuptools import setup, find_packages

# retrieving version
f   = open(os.path.join('kubem', 'version'), 'r')
ver = f.readline()
f.close()

setup(
    name        = 'kubem',
    version     = ver,
    description = 'Python library for building energy management',
    author      = 'Marco A. Alsina',
    author_email= 'marco.alsina@utalca.cl',
    url         = 'https://github.com/marcoalsina/araucaria',
    license     = 'BSD',
    test_suite  = 'tests',
    packages    = find_packages(),
    long_description = open('README.md').read(),
    include_package_data = True,
    install_requires = [
        'numpy>=1.16.4',
        'scipy>=1.3.1',
        'pandas>=1.2.4',
        'geopy>=2.1.0',
        'pyproj>=2.6.0',
        'matplotlib>=3.1.0',
    ],
)
