===================
Material for Sphinx
===================

This theme provides a responsive Material Design theme for Sphinx
documentation. It derives heavily from
`Material for MkDocs <https://squidfunk.github.io/mkdocs-material/>`_,
and also uses code from
`Guzzle Sphinx Theme <https://github.com/guzzle/guzzle_sphinx_theme>`_.

Getting Started
---------------
Install from git

.. code-block:: bash

   pip install git+https://github.com/openforcefield/openff-sphinx-theme.git@master

Or, add to your ReadTheDocs environment.yml

.. code-block:: yml
    dependencies:
        - pip
        # --- Snip --- #
        - pip:
            - git+https://github.com/openforcefield/openff-sphinx-theme.git@master

Update your ``conf.py`` with the required changes:

.. code-block:: python

    html_theme = 'sphinx_material'


There are a lot more ways to customize this theme. See :ref:`Customization`
or ``theme.conf`` for more details.

.. code-block:: python
    html_theme = "openff_sphinx_theme"

    # (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
    # Path should be relative to the ``_static`` files directory.
    # If not provided, will default to the generic OpenFF logo
    html_logo = "_static/images/logos/openff_toolkit_v1_white-on-darkblue.svg"

    # Specify a favicon. The OpenFF logo is provided by the theme in the following file, so you can use it without providing a favicon.
    html_favicon = "_static/images/favicon.svg"

    # Theme options are theme-specific and customize the look and feel of a
    # theme further.
    html_theme_options = {
        # Repository integration
        # Set the repo url for the link to appear
        "repo_url": "https://github.com/openforcefield/openff-toolkit",
        # The name of the repo. If must be set if repo_url is set
        "repo_name": "openff-toolkit",
        # Must be one of github, gitlab or bitbucket
        "repo_type": "github",
        # Colour for sidebar captions and other accents. One of
        # openff-toolkit-blue, openff-dataset-yellow, openff-evaluator-orange,
        # red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
        # teal, green, light-green, lime, yellow, amber, orange, deep-orange
        "color_accent": "openff-toolkit-blue",
        # Content Minification for deployment, prettification for debugging
        "html_minify": True,
        "html_prettify": False,
        "css_minify": True
    }

    # Custom sidebar templates, must be a dictionary that maps document names
    # to template names.
    html_sidebars = {
        # By default, don't show the local table of contents
        "**": ["logo-text.html", "globaltoc.html", "searchbox.html"],
        # On long pages, show the local TOC instead of expanding the global TOC
        # for the current page
        "developing": [
            "logo-text.html",
            "globaltoc.html",
            "searchbox.html",
            "localtoc.html",
        ],
        "faq": [
            "logo-text.html",
            "globaltoc.html",
            "searchbox.html",
            "localtoc.html",
        ],
    }

.. toctree::
    :caption: Basic Use
    :maxdepth: 1

    customization
    specimen
    additional_samples


.. toctree::
    :caption: Other Examples and Uses
    :maxdepth: 1

    pymethod
    numpydoc
    notebook.ipynb
    markdown.md
    rst-cheatsheet/rst-cheatsheet
    basics

.. toctree::
    :caption: Changes and License
    :maxdepth: 1

    change-log
    license



Index
~~~~~
:ref:`genindex`
