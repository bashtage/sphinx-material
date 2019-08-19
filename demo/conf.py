project = u'Demo'
copyright = u'2015, My Name'
master_doc = 'index'
templates_path = ['_templates']
extensions = ['sphinx.ext.todo']
source_suffix = '.rst'
version = 'X.Y.Z'
exclude_patterns = ['_build']
html_short_title = 'Demo Docs'
# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    '**': ['logo-text.html',
           'globaltoc.html',
           'localtoc.html',
           'searchbox.html']
}

import material_sphinx_theme

extensions.append("material_sphinx_theme")
html_theme_path = material_sphinx_theme.html_theme_path()
html_theme = 'material_sphinx_theme'

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "http://my-site.com/docs/"
}

language = 'en'
html_last_updated_fmt = ''
