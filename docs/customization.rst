.. _customization:

=============
Customization
=============

There are two methods to alter the theme.
The first, and simplest, uses the options exposed through ``html_theme_options`` in ``conf.py``.
This site's options are:

.. literalinclude:: conf.py
   :language: python
   :lines: 90-160
   :lineno-start: 90
   :linenos:

Many of these settings are provided in this site as examples; for a minimalistic example, see :ref:`quickstart`.

Configuration Options
=====================

``google_analytics_account``
   Set to enable google analytics.
``repo_url``
   Set the repo url for the link to appear.
``repo_name``
   The name of the repo.
   It must be set if repo_url is set.
``repo_type``
   Must be one of github, gitlab or bitbucket.
``globaltoc_depth``
   The maximum depth of the global TOC; set it to -1 to allow unlimited depth.
``globaltoc_collapse``
   If true, TOC entries that are not ancestors of the current page are collapsed.
``globaltoc_includehidden``
   If true, the global TOC tree will also contain hidden entries.
``color_accent``
    Accent color. Options are
    openff-blue, openff-toolkit-blue, openff-yellow, openff-orange
    aquamarine, lilac, amaranth, grape, violet, pink, pale-green,
    green, crimson, eggplant, turquoise, or any valid CSS color.
``html_minify``
   Minify pages after creation using htmlmin.
``html_prettify``
   Prettify pages, usually only for debugging.
``css_minify``
   Minify css files found in the output directory.
``master_doc``
   Include the master document at the top of the page in the breadcrumb bar.
``nav_links``
   A list of dictionaries where each has three keys:

   - ``href``: The URL or pagename (str)
   - ``title``: The title to appear (str)
   - ``internal``: Flag indicating to use pathto to find the page.  Set to False for external content. (bool)
``heroes``
   A ``dict[str,str]`` where the key is a pagename and the value is the text to display in the page's hero location.
``socials``
   ``list[dict[str, str]]`` of social media links.
   Dicts have three keys: ``"href"``, ``"icon_classes"``, and optionally ``"title"``.
   Icon classes should be from `Academicons <https://jpswalsh.github.io/academicons/>`_ or `Font Awesome 5 <https://fontawesome.com/>`_.
   If not specified, defaults to a set of links appropriate for an OpenFF Initiative project.

Sidebars
========
You must set ``html_sidebars`` in order for the side bar to appear.
There are four in the complete set.

.. code-block:: python

   html_sidebars = {
       "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
   }


You can exclude any to hide a specific sidebar.
For example, if this is changed to

.. code-block:: python

   html_sidebars = {
       "**": ["globaltoc.html"]
   }

then only the global ToC would appear on all pages (``**`` is a glob pattern).

Customizing the layout
======================

You can customize the theme by overriding Jinja template blocks.
For example, 'layout.html' contains several blocks that can be overridden or extended.

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

New Blocks
==========
The theme has a small number of new blocks to simplify some types of
customization:

``footerrel``
   Previous and next in the footer.
``fonticon``
   Block that contains the icon font. You should probably call ``{{ super() }}`` at the end of the block to include the default icon fonts as well. (Font Awesome and Academicons)

