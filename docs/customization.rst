=============
Customization
=============

There are two methods to alter the theme.  The first, and simplest, uses the
options exposed through ``html_theme_options`` in ``conf.py``. This site's
options are:

.. code-block:: python

    html_theme_options = {
        'base_url': 'http://bashtage.github.io/sphinx-material/',
        'repo_url': 'https://github.com/bashtage/sphinx-material/',
        'repo_name': 'Material for Sphinx',
        'google_analytics_account': 'UA-XXXXX',
        'html_minify': True,
        'css_minify': True,
        'nav_title': 'Material Sphinx Demo',
        'logo_icon': '&#xe869',
        'globaltoc_depth': 2
    }

The complete list of options with detailed explanations appears in
``theme.conf``.




Customizing the layout
======================

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
