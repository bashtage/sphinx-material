.. _quickstart:

==============================
OpenFF Sphinx theme Quickstart
==============================

This theme provides a responsive theme for Sphinx documentation by the Open Force Field Initiative.
It is inspired by `Material for Sphinx <https://squidfunk.github.io/mkdocs-material/>`_ and `Material for MkDocs <https://squidfunk.github.io/mkdocs-material/>`_, but has been rewritten with the `Bulma <https://bulma.io>`_ CSS framework to remove any JavaScript dependencies.

Getting Started
---------------
Install from git

.. code-block:: bash

   pip install git+https://github.com/openforcefield/openff-sphinx-theme.git@main

Or, add to your ReadTheDocs environment.yml

.. code-block:: yaml

    dependencies:
        - pip
        - <conda dependency>
        - <conda dependency>
        - <conda dependency>
        # --- snip --- #
        - pip:
            - git+https://github.com/openforcefield/openff-sphinx-theme.git@main

Update your ``conf.py`` with the required changes:

.. code-block:: python

    extensions.append("openff_sphinx_theme")
    html_theme = "openff_sphinx_theme"
    html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}


There are a lot more ways to customize this theme. See :ref:`Customization`
or ``theme.conf`` for more details.

.. code-block:: python

    # Enable the theme itself
    extensions.append("openff_sphinx_theme")
    html_theme = "openff_sphinx_theme"

    # (Optional) Logo in PNG format.
    # If not provided, will default to the generic OpenFF logo with text
    html_logo = "_static/images/logos/openforcefield_v1_white.png"

    # (Optional) favicon.
    # If not provided, will default to the generic OpenFF logo
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
        # openff-blue, openff-toolkit-blue, openff-dataset-yellow,
        # openff-evaluator-orange, aquamarine, lilac, amaranth, grape,
        # violet, pink, pale-green, green, crimson, eggplant, turquoise,
        # or a tuple of three ints in the range [0, 255] corresponding to
        # a position in RGB space.
        "color_accent": "openff-toolkit-blue",
        # Content Minification for deployment, prettification for debugging
        "html_minify": True,
        "html_prettify": False,
        "css_minify": True,
    }

    # Custom sidebar templates, must be a dictionary that maps document names
    # to template names.
    html_sidebars = {
        # By default, show everything
        "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
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
    pydantic
    notebook.ipynb
    markdown.md
    rst-cheatsheet/rst-cheatsheet
    primer

.. toctree::
    :caption: Changes and License
    :maxdepth: 1

    change-log
    license



Index
~~~~~
:ref:`genindex`
