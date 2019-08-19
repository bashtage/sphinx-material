=====================
Material Sphinx Theme
=====================

Installation
============

Install via pip::

    $ pip install material_sphinx_theme

or if you have the code checked out locally::

    $ python setup.py install

Configuration
=============

Add the following to your conf.py:

.. code-block:: python

    import material_sphinx_theme

    html_theme_path = material_sphinx_theme.html_theme_path()
    html_theme = 'material_sphinx_theme'

    # Register the theme as an extension to generate a sitemap.xml
    extensions.append("material_sphinx_theme")

    # Material theme options (see theme.conf for more information)
    html_theme_options = {
        # Set the name of the project to appear in the sidebar
        "project_nav_name": "Project Name",
    }

There are a lot more ways to customize this theme, as this more comprehensive
example shows:

.. code-block:: python

    import material_sphinx_theme

    html_theme_path = material_sphinx_theme.html_theme_path()
    html_theme = 'material_sphinx_theme'

    # Register the theme as an extension to generate a sitemap.xml
    extensions.append("material_sphinx_theme")

    # Material theme options (see theme.conf for more information)
    html_theme_options = {

        # Set the path to a special layout to include for the homepage
        "index_template": "special_index.html",

        # Set the name of the project to appear in the left sidebar.
        "project_nav_name": "Project Name",

        # Set your Disqus short name to enable comments
        "disqus_comments_shortname": "my_disqus_comments_short_name",

        # Set you GA account ID to enable tracking
        "google_analytics_account": "my_ga_account",

        # Path to a touch icon
        "touch_icon": "",

        # Specify a base_url used to generate sitemap.xml links. If not
        # specified, then no sitemap will be built.
        "base_url": "",

        # Allow a separate homepage from the master_doc
        "homepage": "index",

        # Allow the project link to be overriden to a custom URL.
        "projectlink": "http://myproject.url",

        # Visible levels of the global TOC; -1 means unlimited
        "globaltoc_depth": 3,

        # If False, expand all TOC entries
        "globaltoc_collapse": False,

        # If True, show hidden TOC entries
        "globaltoc_includehidden": False,
    }

Customizing the layout
======================

You can customize the theme by overriding Jinja template blocks. For example,
"layout.html" contains several blocks that can be overridden or extended.

Place a "layout.html" file in your project's "/_templates" directory.

.. code-block:: bash

    mkdir source/_templates
    touch source/_templates/layout.html

Then, configure your "conf.py":

.. code-block:: python

    templates_path = ['_templates']

Finally, edit your override file "source/_templates/layout.html":

::

    {# Import the theme's layout. #}
    {% extends "!layout.html" %}

    {%- block extrahead %}
    {# Add custom things to the head HTML tag #}
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}

.. note::

  If you are using Readthedocs, then you might run into an issue where they
  don't currently allow you to extend layout.html.
