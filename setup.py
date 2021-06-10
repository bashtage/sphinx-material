from setuptools import setup

import versioneer

with open("requirements.txt") as reqs:
    REQUIREMENTS = [reqs.readlines()]

with open("requirements-dev.txt") as dev_reqs:
    REQUIREMENTS_DEV = [dev_reqs.readlines()]

setup(
    name="openff-sphinx-theme",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Sphinx theme for Open Force Field projects",
    long_description=open("README.rst").read(),
    author="Open Force Field Initiative",
    url="https://github.com/openforcefield/openff-sphinx-theme",
    packages=["openff-sphinx-theme"],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    extras_require={"dev": REQUIREMENTS_DEV},
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx :: Theme",
        "Topic :: Documentation :: Sphinx",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        "sphinx.html_themes": [
            "openff-sphinx-theme=openff-sphinx-theme",
        ]
    },
)
