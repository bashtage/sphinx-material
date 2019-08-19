from setuptools import setup

setup(
    name='material_sphinx_theme',
    version='0.7.11',
    description='Material sphinx theme',
    long_description=open('README.rst').read(),
    author='Kevin Sheppard',
    author_email='kevin.k.sheppard@gmail.com',
    url='https://github.com/bashtage/material_sphinx_theme',
    packages=['material_sphinx_theme'],
    include_package_data=True,
    install_requires=['Sphinx>1.3'],
    license="MIT",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: NSCA License',
        'Programming Language :: Python',
    ),
)
