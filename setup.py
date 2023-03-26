import codecs
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

INSTALL_REQUIRES = [
    "aiogram"
]

setup(
    name="bot",
    version="1.0.0",
    description="The implementation of a telegram chat bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["bot"],
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)