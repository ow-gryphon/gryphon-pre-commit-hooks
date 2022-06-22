"""
Setup module.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='ignore-files-pre-commit-hook',
    version='0.1.0',
    license='MIT',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['main'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        ignore-files=ignore_files:main
    '''
)
