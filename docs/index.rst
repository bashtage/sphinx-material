===================
Material for Sphinx
===================

This theme provides a responsive Material Design theme for Sphinx
documentation. It is inspired by
`Material for Sphinx <https://squidfunk.github.io/mkdocs-material/>`_ and
`Material for MkDocs <https://squidfunk.github.io/mkdocs-material/>`_, but has been rewritten from scratch with the `Bulma <https://bulma.io>`_ CSS framework.

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


There are a lot more ways to customize this theme. See :ref:`Customization`
or ``theme.conf`` for more details.

.. code-block:: python

    # Enable the theme itself
    extensions.append("openff_sphinx_theme")
    html_theme = "openff_sphinx_theme"

    # (Optional) Logo.
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
        # openff-blue, openff-toolkit-blue, openff-yellow, openff-orange
        # aquamarine, lilac, amaranth, grape, violet, pink, pale-green,
        # green, crimson, eggplant, turquoise, or any valid CSS color.
        "color_accent": "openff-toolkit-blue",
        # Content Minification for deployment, prettification for debugging
        "html_minify": True,
        "html_prettify": False,
        "css_minify": True,
        # Social media links for the footer
        # Must be a list of dicts with three keys: "href", "icon_classes",
        # and optionally "title". Icon classes should be from Academicons or
        # Font Awesome
        "socials": [
            {
                "href": "https://zenodo.org/communities/openforcefield/",
                "title": "OpenFF on Zenodo",
                "icon_classes": "ai ai-zenodo",
            },
            {
                "href": "https://www.youtube.com/channel/UCh0aJSUm_sYr7nuTzhW806g",
                "title": "OpenFF on YouTube",
                "icon_classes": "fab fa-youtube",
            },
            {
                "href": "https://github.com/openforcefield",
                "title": "OpenFF on GitHub",
                "icon_classes": "fab fa-github",
            },
            {
                "href": "https://twitter.com/openforcefield",
                "title": "OpenFF on Twitter",
                "icon_classes": "fab fa-twitter",
            },
            {
                "href": "https://www.linkedin.com/company/openforcefield/",
                "title": "OpenFF on LinkedIn",
                "icon_classes": "fab fa-linkedin",
            },
        ],
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
    primer

.. toctree::
    :caption: Changes and License
    :maxdepth: 1

    change-log
    license



Index
~~~~~
:ref:`genindex`
