.. _customization:

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

Configuration Options
=====================

``nav_title``
   Set the name to appear in the left sidebar/header. If not provided, uses
   html_short_title if defined, or html_title.
``touch_icon``
   Path to a touch icon, should be 152x152 or larger.
``google_analytics_account``
   Set to enable google analytics.
``repo_url``
   Set the repo url for the link to appear.
``repo_name``
   The name of the repo. If must be set if repo_url is set.
``repo_type``
   Must be one of github, gitlab or bitbucket.
``base_url``
   Specify a base_url used to generate sitemap.xml links. If not specified, then
   no sitemap will be built.
``globaltoc_depth``
   The maximum depth of the global TOC; set it to -1 to allow unlimited depth.
``globaltoc_collapse``
   If true, TOC entries that are not ancestors of the current page are collapsed.
``globaltoc_includehidden``
   If true, the global TOC tree will also contain hidden entries.
``theme_color``
    The theme color for mobile browsers. Hex Color without the leading #.
``color_primary``
    Primary colo. Options are
    red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
    teal, green, light-green, lime, yellow, amber, orange, deep-orange,
    brown, grey, blue-grey, and white.
``color_accent``
    Accent color. Options are
    red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
    teal, green, light-green, lime, yellow, amber, orange, and deep-orange.
``html_minify``
   Minify pages after creation using htmlmin.
``html_prettify``
   Prettify pages, usually only for debugging.
``css_minify``
   Minify css files found in the output directory.
``logo_icon``
   Set the logo icon. Should be a pre-escaped html string that indicates a
   unicode point, e.g., ``'&#xe869'`` which is used on this site.

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

Finally, edit your override file ``source/_templates/layout.html``:

.. code-block:: jinja

    {# Import the theme's layout. #}
    {% extends '!layout.html' %}

    {%- block extrahead %}
    {# Add custom things to the head HTML tag #}
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}
