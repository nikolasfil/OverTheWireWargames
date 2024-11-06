import setuptools
import os

with open("app/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wargame-framework",
    version="0.0.1",
    description="A framework to easily connect to overthewire wargames ",
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikolasfil/OverTheWireWargames",
    author="Nikolas Filippatos",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "argcomplete>=3.5.1",
        "pyperclip>=1.9.0",
    ],
    extras_require={
        "dev": ["pytest>=6.2.4", "twine>=3.4.2"],
    },
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            # "folders=ctfsolver.folders.__main__:main",
            "find_usage=ctfsolver.scripts.run_find_usage:main",
        ]
    },
)
