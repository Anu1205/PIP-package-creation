from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A basic sum of N natural numbers computation package'
#LONG_DESCRIPTION = 'A package that allows to build sum of N natural numbers'

# Setting up
setup(
    name="SumNnumbers",
    version=VERSION,
    author="AnushaKaligota",
    author_email="<anusha.kaligota@gmail.com>",
    description=DESCRIPTION,
#     long_description_content_type="text/markdown",
#     long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)