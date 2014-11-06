"""
Standard Setup script
"""
from setuptools import setup, find_packages

setup(
    name="Flask-JsonSchemaValidator",
    version="0.1",
    packages=find_packages(),
    author="William Clemens",
    author_email="wesclemens@gmail.com",
    license="MIT",
    url="https://github.com/wesclemens/Flask-JsonSchemaValidator",
    install_requires=[
        'Flask>=0.10.1',
        'decorators>=0.1',
        'jsonschema>=2.4.0',
    ],
)
