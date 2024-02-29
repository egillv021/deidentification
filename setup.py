from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='deidentification',
    version='0.1',
    packages=find_packages(),
    install_requires=required_packages,
    # other metadata for your package
)