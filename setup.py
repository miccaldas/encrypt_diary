from setuptools import setup

setup(
    name="encrypt_diary",
    version=2.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Digital diary with encryption.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/encrypt_diary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["encrypt_diary"],
    install_requires=[
        "colr",
        "getpass",
        "peewee",
        "loguru",
        "playhouse.sqlcipher_ext",
    ],
    include_package_data=True,
)
