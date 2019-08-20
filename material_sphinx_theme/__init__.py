"""Sphinx Material theme."""

import os
import xml.etree.ElementTree as ET

from sphinx.writers.html5 import HTML5Translator as _HTML5Translator


def setup(app):
    """Setup conntects events to the sitemap builder"""
    app.connect('html-page-context', add_html_link)
    app.connect('build-finished', create_sitemap)
    app.set_translator('html', HTMLTranslator)
    app.sitemap_links = []


def add_html_link(app, pagename, templatename, context, doctree):
    """As each page is built, collect page names for the sitemap"""
    base_url = app.config['html_theme_options'].get('base_url', '')
    if base_url:
        app.sitemap_links.append(base_url + pagename + ".html")


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    if (not app.config['html_theme_options'].get('base_url', '') or
           exception is not None or
           not app.sitemap_links):
        return

    filename = app.outdir + "/sitemap.xml"
    print("Generating sitemap.xml in %s" % filename)

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = link

    ET.ElementTree(root).write(filename)


def html_theme_path():
    return [os.path.dirname(os.path.abspath(__file__))]


class HTMLTranslator(_HTML5Translator):
    """
    Handle translating to bootstrap structure.
    """
    pass


def toctree_format(toc_text):
    from bs4 import BeautifulSoup

    toc = BeautifulSoup(toc_text, features='html.parser')
    toc.ul['class'] = 'md-nav__list'
    toc.ul['data-md-scrollfix'] = None
    for li in toc.ul.select('li'):
        li['class'] = 'md-nav__item'
        for a in li.select('a'):
            a['class'] = 'md-nav__link'
    return str(toc)


def toc_format(toc_text):
    from bs4 import BeautifulSoup
    import slugify
    toc = BeautifulSoup(toc_text, features='html.parser')
    for ul in toc.select('ul'):
        ul['class'] = 'md-nav__list'
    for li in toc.select('li'):
        li['class'] = 'md-nav__item'
    for a in toc.select('a'):
        if a['href'] == '#' and a.contents:
            a['href'] = '#' + slugify.slugify(a.contents[0])
        a['class'] = 'md-nav__link'
    toc.ul['data-md-scrollfix'] = None
    return str(toc)


def table_fix(body_text):
    from bs4 import BeautifulSoup
    import re

    body = BeautifulSoup(body_text, features='html.parser')
    for table in body.select('table'):
        classes = table.get('class', tuple())
        if 'highlighttable' in classes or 'longtable' in classes:
            continue
        del table['class']
    headers = body.find_all(re.compile('^h[1-6]$'))
    for i, header in enumerate(headers):
        for a in header.select('a'):
            if 'headerlink' in a.get('class', ''):
                header['id'] = a['href'][1:]
    divs = body.find_all('div', {'class': 'section'})
    for div in divs:
        div.unwrap()

    return str(body)


def get_html_context():
    return {'toctree_format': toctree_format,
            'toc_format': toc_format,
            'table_fix': table_fix}
