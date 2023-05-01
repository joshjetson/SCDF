from setuptools import setup, find_packages

from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="streamlit_controllerDF",
    version="0.1.3",
    description="A solid base for controlling your data frame, getting quick metrics, and data visualizations using streamlit, pandas, numpy and matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshjetson/SCDF/",
    author="Joshua Dario",
    author_email="joshuajdr@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["streamlit","pandas","matplotlib","numpy"],
    keywords=['Python','streamlit','dataframe','data frame','data set',
    'visualization','automatic','widgets','automation','machine learning',
    'quick','controller','controllerdf','controllerDF','streamlit controller','streamlit data frame',
    'streamlit controllerDF']
)
