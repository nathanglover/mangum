from setuptools import find_packages, setup

from mangum.__version__ import __version__


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="mangum",
    version=__version__,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/erm/mangum",
    description="AWS Lambda & API Gateway support for ASGI",
    long_description=get_long_description(),
    python_requires=">=3.6",
    install_requires=["typing_extensions", "dataclasses; python_version < '3.7'"],
    extras_require={"full": ["boto3"]},
    package_data={"mangum": ["py.typed"]},
    long_description_content_type="text/markdown",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
