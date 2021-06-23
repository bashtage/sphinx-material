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

More customization options can be found in the `demonstration site <https://openforcefield.github.io/openff-sphinx-theme/>`_.

.. |MIT License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT-Clause
