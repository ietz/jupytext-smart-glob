from pathlib import Path
from setuptools import setup, find_packages

# The directory containing this file
here = Path(__file__).parent

# The text of the README file
readme = (here / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='jupytext-smart-glob',
    version='1.0.0',
    description='Automatically detect Jupytext files to transform into Notebooks',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ietz/jupytext-smart-glob',
    author='Tim Pietz',
    author_email='tim@pietz.me',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jupytext',
        'nbformat',
    ],
)
