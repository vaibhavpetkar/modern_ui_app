# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="modern_ui_app",
    version="0.0.1",
    description="Modern UI Theme for ERPNext",
    author="Manus AI",
    author_email="noreply@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["frappe"],
)
