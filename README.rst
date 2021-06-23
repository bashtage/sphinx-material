Material Sphinx Theme
=====================

**License**

|MIT License|

A Material Design theme for Sphinx documentation.
Based on `Material for Sphinx <https://bashtage.github.io/sphinx-material/>`_.

See the theme's `demonstration site <https://openforcefield.github.io/openff-sphinx-theme/>`_ for examples of rendered rst and more detailed instructions.

Getting Started
---------------

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
    
There are some basic customization options you probably also wanna set:

.. code-block:: python

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

More customization options can be found in the `demonstration site <https://openforcefield.github.io/openff-sphinx-theme/>`_.

.. |MIT License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT-Clause
