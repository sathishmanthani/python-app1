import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-app1",
    version="1.0.0",
    description="First python app and its deployment",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sathishmanthani/pytest/tree/master",
    author="Sathish Manthani",
    author_email="dummy@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["python-app1"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=python-app1.__main__:main",
        ]
    },
)