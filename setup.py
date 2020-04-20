from setuptools import setup

import versioneer

REQUIREMENTS = [
    'sphinx>=2.0',
    'beautifulsoup4',
    'python-slugify[unidecode]',
    'css_html_js_minify',
    'lxml',
]

REQUIREMENTS_DEV = [
    'black==19.10b0',
]

setup(
    name="sphinx_material",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Material sphinx theme",
    long_description=open("README.rst").read(),
    author="Kevin Sheppard",
    author_email="kevin.k.sheppard@gmail.com",
    url="https://github.com/bashtage/sphinx-material",
    packages=["sphinx_material"],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': REQUIREMENTS_DEV,
    },
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
)
