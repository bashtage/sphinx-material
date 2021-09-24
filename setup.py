import setuptools

import atexit
import distutils.command.build
import os
import subprocess
import tempfile

import setuptools.command.build_py
import setuptools.command.develop
import setuptools.command.install
import setuptools.command.sdist
import versioneer

with open("requirements.txt") as reqs:
    REQUIREMENTS = [reqs.readlines()]

with open("requirements-dev.txt") as dev_reqs:
    REQUIREMENTS_DEV = [dev_reqs.readlines()]

root_dir = os.path.dirname(os.path.abspath(__file__))
package_root = os.path.join(root_dir, 'sphinx_material')


def _setup_temp_egg_info(cmd):
    """Use a temporary directory for the `neuroglancer.egg-info` directory.

    When building an sdist (source distribution) or installing, locate the
    `sphinx_material.egg-info` directory inside a temporary directory so that it
    doesn't litter the source directory and doesn't pick up a stale SOURCES.txt
    from a previous build.
    """
    egg_info_cmd = cmd.distribution.get_command_obj('egg_info')
    if egg_info_cmd.egg_base is None:
        tempdir = tempfile.TemporaryDirectory(dir=os.curdir)
        egg_info_cmd.egg_base = tempdir.name
        atexit.register(tempdir.cleanup)


class SdistCommand(setuptools.command.sdist.sdist):
    def run(self):
        _setup_temp_egg_info(self)
        self.run_command('static_bundles')
        super().run()

    def make_release_tree(self, base_dir, files):
        # Exclude .egg-info from source distribution.  These aren't actually
        # needed, and due to the use of the temporary directory in `run`, the
        # path isn't correct if it gets included.
        files = [x for x in files if '.egg-info' not in x]
        super().make_release_tree(base_dir, files)


class InstallCommand(setuptools.command.install.install):
    def run(self):
        _setup_temp_egg_info(self)
        self.run_command('static_bundles')
        super().run()


class BuildCommand(distutils.command.build.build):
    def finalize_options(self):
        if self.build_base == 'build':
            # Use temporary directory instead, to avoid littering the source directory
            # with a `build` sub-directory.
            tempdir = tempfile.TemporaryDirectory()
            self.build_base = tempdir.name
            atexit.register(tempdir.cleanup)
        super().finalize_options()

    def run(self):
        _setup_temp_egg_info(self)
        self.run_command('static_bundles')
        super().run()


class DevelopCommand(setuptools.command.develop.develop):
    def run(self):
        self.run_command('static_bundles')
        super().run()


class StaticBundlesCommand(setuptools.command.build_py.build_py):

    user_options = setuptools.command.build_py.build_py.user_options + [
        ('bundle-type=', None,
         'The bundle type. "min" (default) creates minified bundles,'
         ' "dev" creates non-minified files.'),
        ('skip-npm-reinstall', None,
         'Skip running `npm install` if the `node_modules` directory already exists.'
         ),
        ('skip-rebuild', None,
         'Skip rebuilding if the `sphinx_material` directory already exists.'),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.bundle_type = 'min'
        self.skip_npm_reinstall = None
        self.skip_rebuild = None

    def finalize_options(self):
        super().finalize_options()
        if self.bundle_type not in ['min', 'dev']:
            raise RuntimeError('bundle-type has to be one of "min" or "dev"')

        if self.skip_npm_reinstall is None:
            self.skip_npm_reinstall = False

        if self.skip_rebuild is None:
            self.skip_rebuild = False

    def run(self):
        if self.skip_rebuild:
            output_dir = os.path.join(package_root, 'static')
            if os.path.exists(output_dir):
                print('Skipping rebuild of package since %s already exists' %
                      (output_dir, ))
                return

        target = {"min": "build", "dev": "build:dev"}

        try:
            t = target[self.bundle_type]
            node_modules_path = os.path.join(root_dir, 'node_modules')
            if (self.skip_npm_reinstall and os.path.exists(node_modules_path)):
                print('Skipping `npm install` since %s already exists' %
                      (node_modules_path, ))
            else:
                subprocess.call('npm i', shell=True, cwd=root_dir)
            res = subprocess.call('npm run %s' % t, shell=True, cwd=root_dir)
        except:
            raise RuntimeError('Could not run \'npm run %s\'.' % t)

        if res != 0:
            raise RuntimeError('failed to build sphinx-material package')


setuptools.setup(
    name="sphinx_material",
    version=versioneer.get_version(),
    description="Material sphinx theme",
    long_description=open("README.rst").read(),
    author="Kevin Sheppard",
    author_email="kevin.k.sheppard@gmail.com",
    url="https://github.com/bashtage/sphinx-material",
    packages=["sphinx_material"],
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
            "sphinx_material = sphinx_material",
        ]
    },
    cmdclass=dict(
        versioneer.get_cmdclass(),
        sdist=SdistCommand,
        build=BuildCommand,
        install=InstallCommand,
        static_bundles=StaticBundlesCommand,
        develop=DevelopCommand,
    ),
)
