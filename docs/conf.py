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

import sphinx_material
from recommonmark.transform import AutoStructify

FORCE_CLASSIC = os.environ.get("SPHINX_MATERIAL_FORCE_CLASSIC", False)
FORCE_CLASSIC = FORCE_CLASSIC in ("1", "true")

# -- Project information -----------------------------------------------------

project = "Material for Sphinx"
html_title = "Material for Sphinx"

copyright = "2019, Kevin Sheppard"
author = "Kevin Sheppard"

# The full version, including alpha/beta/rc tags
#release = LooseVersion(sphinx_material.__version__).vstring
release = '1'

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
    # Disable nbsphinx since it greatly slows down documentation build.
    #"nbsphinx",
    "recommonmark",
    "sphinx_markdown_tables",
]

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# -- HTML theme settings ------------------------------------------------

extensions.append("sphinx_material")
html_theme = "sphinx_material"

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "logo": "material/library",
    },
    "site_url": "http://bashtage.github.io/sphinx-material/",
    "repo_url": "https://github.com/bashtage/sphinx-material/",
    "repo_name": "Material for Sphinx",
    "repo_type": "github",
    "google_analytics": ["UA-XXXXX", "auto"],
    "html_minify": False,
    "html_prettify": False,
    "css_minify": False,
    'globaltoc_collapse': True,
    "globaltoc_depth": -1,
    'features': [
        # 'navigation.expand',
        # 'navigation.tabs',
        # 'toc.integrate',
        'navigation.sections',
        # 'navigation.instant',
        # 'header.autohide',
        'navigation.top',
    ],
    'palette': [
        {
        'media': '(prefers-color-scheme: light)',
        'scheme': 'default',
        'primary': 'blue',
        'accent': 'cyan',
            'toggle': {
                'icon': 'material/lightbulb-outline',
                'name': 'Switch to dark mode',
            },
    },
        {
        'media': '(prefers-color-scheme: dark)',
        'scheme': 'slate',
        'primary': 'blue',
        'accent': 'cyan',
            'toggle': {
                'icon': 'material/lightbulb',
                'name': 'Switch to light mode',
            },
    },
    ],
    "touch_icon": "images/apple-icon-152x152.png",
    "heroes": {
        "index": "A responsive Material Design theme for Sphinx sites.",
        "customization": "Configuration options to personalize your site.",
    },
    "version_dropdown": True,
    "version_json": "_static/versions.json",
    "version_info": [
        {
            "title": "Release",
            "version": "https://bashtage.github.io/sphinx-material/",
            "aliases": []
        },
        {
            "title": "Development",
            "version": "https://bashtage.github.io/sphinx-material/devel/",
            "aliases": []
        },
        {
            "title": "Release (rel)",
            "version": "/sphinx-material/",
            "aliases": []
        },
        {
            "title": "Development (rel)",
            "version": "/sphinx-material/devel/",
            "aliases": []
        },
    ],
}

if FORCE_CLASSIC:
    print("!!!!!!!!! Forcing classic !!!!!!!!!!!")
    html_theme = "classic"
    html_theme_options = {}
    html_sidebars = {
        "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
    }

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True
html_favicon = "images/favicon.ico"

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


# Enable eval_rst in markdown
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "enable_math": True,
            "enable_inline_math": True,
            "enable_eval_rst": True
        },
        True,
    )
    app.add_transform(AutoStructify)
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )

# Use MathJax 3.
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
