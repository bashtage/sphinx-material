from setuptools import setup

setup(
    name='sphinx_material',
    version='0.1.0',
    description='Material sphinx theme',
    long_description=open('README.rst').read(),
    author='Kevin Sheppard',
    author_email='kevin.k.sheppard@gmail.com',
    url='https://github.com/bashtage/sphinx-material',
    packages=['sphinx_material'],
    include_package_data=True,
    install_requires=['Sphinx>2.0',
                      'python-slugify',
                      'unidecode',
                      'beautifulsoup4'],
    license="MIT",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
