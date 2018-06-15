import codecs
import os
from setuptools import setup, find_packages

import lidarrstats

HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='lidarrstats',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=lidarrstats.__version__,  # Required

    description='Lidarr stats server',  # Required
    long_description=LONG_DESCRIPTION,  # Optional
    url='https://github.com/lidarr/LidarrAPI.Stats',  # Optional
    author='Lidarr',  # Optional
    author_email='development@lidarr.audio',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    install_requires=[
        'flask',
        'flask-restful',
        'rethinkdb'
    ],  # Optional

    extras_require={
        'deploy': ['gunicorn']
    }
)