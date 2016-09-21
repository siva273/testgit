from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='diya',
    version='0.0.1',
    long_description=readme,
    license=license(),
    packages=find_packages(exclude=('test', 'docs'))
)