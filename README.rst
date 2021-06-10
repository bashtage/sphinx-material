Material Sphinx Theme
=====================

**Continuous Integration**

|Travis Build Status|

**Release**

|PyPI Status|

**License**

|MIT License|

A Material Design theme for Sphinx documentation.
Based on `Material for MkDocs <https://squidfunk.github.io/mkdocs-material/>`_, and `Guzzle Sphinx Theme <https://github.com/guzzle/guzzle_sphinx_theme>`_.

See the theme's `demonstration site <https://openforcefield.github.io/openff-sphinx-theme/>`_ for examples of rendered rst.

Configuration
-------------

Add the following to your conf.py:

.. code-block:: python

    html_theme = 'openff_sphinx_theme'


There are a lot more ways to customize this theme, as this more comprehensive
example shows:

.. code-block:: python

    # Required theme setup
    html_theme = 'openff_sphinx_theme'

    # Set link name generated in the top bar.
    html_title = 'Project Title'

    # Material theme options (see theme.conf for more information)
    html_theme_options = {

        # Set the name of the project to appear in the navigation.
        'nav_title': 'Project Name',

        # Set you GA account ID to enable tracking
        'google_analytics_account': 'UA-XXXXX',

        # Specify a base_url used to generate sitemap.xml. If not
        # specified, then no sitemap will be built.
        'base_url': 'https://project.github.io/project',

        # Set the color and the accent color
        'color_primary': 'blue',
        'color_accent': 'light-blue',

        # Set the repo location to get a badge with stats
        'repo_url': 'https://github.com/project/project/',
        'repo_name': 'Project',

        # Visible levels of the global TOC; -1 means unlimited
        'globaltoc_depth': 3,
        # If False, expand all TOC entries
        'globaltoc_collapse': False,
        # If True, show hidden TOC entries
        'globaltoc_includehidden': False,
    }

Customizing the layout
----------------------

You can customize the theme by overriding Jinja template blocks. For example,
'layout.html' contains several blocks that can be overridden or extended.

Place a 'layout.html' file in your project's '/_templates' directory.

.. code-block:: bash

    mkdir source/_templates
    touch source/_templates/layout.html

Then, configure your 'conf.py':

.. code-block:: python

    templates_path = ['_templates']

Finally, edit your override file 'source/_templates/layout.html':

::

    {# Import the theme's layout. #}
    {% extends '!layout.html' %}

    {%- block extrahead %}
    {# Add custom things to the head HTML tag #}
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}

.. |Travis Build Status| image:: https://travis-ci.org/openforcefield/openff-sphinx-theme.svg?branch=master
   :target: https://travis-ci.org/openforcefield/openff-sphinx-theme

.. |MIT License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT-Clause
