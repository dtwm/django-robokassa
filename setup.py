#!/usr/bin/env python
from setuptools import setup


setup(
    name="django-robokassa3",
    version="1.4",
    author="Mikhail Pyrev",
    author_email="mikhail.pyrev@gmail.com",
    packages=["robokassa", "robokassa.migrations"],
    url="https://github.com/mpyrev/django-robokassa",
    license="MIT License",
    description="Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.",
    long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
    install_requires=["Django>2"],
    classifiers=(
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: Russian",
    ),
)
