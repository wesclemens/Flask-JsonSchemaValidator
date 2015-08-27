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
        'jsonschema>=2.4.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='Flask jsonschema validation',
)
