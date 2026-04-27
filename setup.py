"""Python setup.py for tmh_test package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("tmh_test", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="tmh_test",
    version=read("tmh_test", "VERSION"),
    description="Awesome tmh_test created by zhanghulu2004",
    url="https://github.com/zhanghulu2004/TMH_test/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="zhanghulu2004",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["tmh_test = tmh_test.__main__:main"]
    },
    extras_require={
        "test": read_requirements("requirements-test.txt")
        + read_requirements("requirements-base.txt")
    },
)
