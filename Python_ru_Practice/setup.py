from setuptools import setup, find_packages
setup(
    name = 'test',
    version='0.1',
    author = 'Andrei Ilyin',
    description = 'First step for python wheel',
    long_description= 'First step for python wheel long description ...',
    packages = find_packages(),
    classifiers = ['Development Status :: 3 - Alpha'],
    requires = [] # Add your dependencies in requirements for example:"setuptools == 75.5.0"
    # Add your dependencies in requirements

)