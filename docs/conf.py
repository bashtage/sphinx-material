# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from distutils.version import LooseVersion
import os

# -- Project information -----------------------------------------------------

project = "OpenFF Sphinx theme"
html_title = "OpenFF Sphinx theme"

copyright = "2021, Open Force Field Initiative"
author = "Open Force Field Initiative"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "myst_parser",
    "openff_sphinx_theme",
]

# Autodoc settings
autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}

# Disable NumPy style attributes/methods expecting every method to have its own docs page
numpydoc_class_members_toctree = False
# Disable numpydoc rendering methods twice
# https://stackoverflow.com/questions/34216659/sphinx-autosummary-produces-two-summaries-for-each-class
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "openff_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
    "customization": ["logo-text.html", "globaltoc.html", "searchbox.html"],
}

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "http://openforcefield.github.io/openff-sphinx-theme/",
    "repo_url": "https://github.com/openforcefield/openff-sphinx-theme/",
    "repo_name": "openff-sphinx-theme",
    "html_minify": False,
    "html_prettify": False,
    "css_minify": False,
    "globaltoc_depth": 2,
    "color_accent": "lilac",
    "nav_links": [
        {
            "href": "https://squidfunk.github.io/mkdocs-material/",
            "internal": False,
            "title": "Material for MkDocs",
        },
        {
            "href": "https://bashtage.github.io/sphinx-material/",
            "internal": False,
            "title": "Material for Sphinx",
        },
        {
            "href": "https://openforcefield.org",
            "internal": False,
            "title": "The Open Force Field Initiative",
        },
        {
            "href": "https://github.com/openforcefield/openff-sphinx-theme/",
            "internal": False,
            "title": "openff-sphinx-theme on GitHub",
        },
    ],
    "heroes": {
        "index": "A responsive Material Design theme for Sphinx sites.",
        "customization": "Configuration options to personalize your site.",
    },
    "table_classes": ["plain"],
}

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        "",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", ""),
    "dudir": ("http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s", ""),
}

# Extensions for the myst parser
myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "smartquotes",
    "replacements",
    "deflist",
]
myst_update_mathjax = False
