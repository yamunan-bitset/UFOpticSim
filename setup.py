from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

setup(
    name='UFOpticSim',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pygame',
        'numpy'
    ],  # Add a comma here
    author='Anirudh Yamunan Govindarajan',
    author_email='yamunan.bitset@gmail.com',
    description='Ultra Fast Optics Simulations with Python3',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
           'Source Repository': 'https://github.com/yamunan-bitset/UFOpticSim/' #replace with your github source
    }
)