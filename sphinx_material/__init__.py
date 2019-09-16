"""Sphinx Material theme."""

import os
import re
import sys
import xml.etree.ElementTree as ET
from multiprocessing import Manager
from typing import List

import bs4
from bs4 import BeautifulSoup
from sphinx.util import logging, console
import slugify

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

ROOT_SUFFIX = "--page-root"


def setup(app):
    """Setup connects events to the sitemap builder"""
    app.connect("html-page-context", add_html_link)
    app.connect("build-finished", create_sitemap)
    app.connect("build-finished", reformat_pages)
    app.connect("build-finished", minify_css)
    manager = Manager()
    site_pages = manager.list()
    sitemap_links = manager.list()
    app.multiprocess_manager = manager
    app.sitemap_links = sitemap_links
    app.site_pages = site_pages
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_html_link(app, pagename, templatename, context, doctree):
    """As each page is built, collect page names for the sitemap"""
    base_url = app.config["html_theme_options"].get("base_url", "")
    if base_url:
        app.sitemap_links.append(base_url + pagename + ".html")
    minify = app.config["html_theme_options"].get("html_minify", False)
    prettify = app.config["html_theme_options"].get("html_prettify", False)
    if minify and prettify:
        raise ValueError("html_minify and html_prettify cannot both be True")
    if minify or prettify:
        app.site_pages.append(os.path.join(app.outdir, pagename + ".html"))


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    if (
        not app.config["html_theme_options"].get("base_url", "")
        or exception is not None
        or not app.sitemap_links
    ):
        return

    filename = app.outdir + "/sitemap.xml"
    print(
        "Generating sitemap for {0} pages in "
        "{1}".format(len(app.sitemap_links), console.colorize("blue", filename))
    )

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = link
    app.sitemap_links[:] = []

    ET.ElementTree(root).write(filename)


def reformat_pages(app, exception):
    if exception is not None or not app.site_pages:
        return
    minify = app.config["html_theme_options"].get("html_minify", False)
    last = -1
    npages = len(app.site_pages)
    transform = "Minifying" if minify else "Prettifying"
    print("{0} {1} files".format(transform, npages))
    transform = transform.lower()
    # TODO: Consider using parallel execution
    for i, page in enumerate(app.site_pages):
        if int(100 * (i / npages)) - last >= 1:
            last = int(100 * (i / npages))
            color_page = console.colorize("blue", page)
            msg = "{0} files... [{1}%] {2}".format(transform, last, color_page)
            sys.stdout.write("\033[K" + msg + "\r")
        with open(page, "r", encoding="utf-8") as content:
            if minify:
                from css_html_js_minify.html_minifier import html_minify

                html = html_minify(content.read())
            else:
                soup = BeautifulSoup(content.read(), features="lxml")
                html = soup.prettify()
        with open(page, "w", encoding="utf-8") as content:
            content.write(html)
    app.site_pages[:] = []
    print()


def minify_css(app, exception):
    if exception is not None or not app.config["html_theme_options"].get(
        "css_minify", False
    ):
        app.multiprocess_manager.shutdown()
        return
    import glob
    from css_html_js_minify.css_minifier import css_minify

    css_files = glob.glob(os.path.join(app.outdir, "**", "*.css"), recursive=True)
    print("Minifying {0} css files".format(len(css_files)))
    for css_file in css_files:
        colorized = console.colorize("blue", css_file)
        msg = "minifying css file {0}".format(colorized)
        sys.stdout.write("\033[K" + msg + "\r")
        with open(css_file, "r", encoding="utf-8") as content:
            css = css_minify(content.read())
        with open(css_file, "w", encoding="utf-8") as content:
            content.write(css)
    print()
    app.multiprocess_manager.shutdown()


def html_theme_path():
    return [os.path.dirname(os.path.abspath(__file__))]


def ul_to_list(node: bs4.element.Tag, fix_root: bool, page_name: str) -> List[dict]:
    out = []
    for child in node.find_all("li", recursive=False):
        if callable(child.isspace) and child.isspace():
            continue
        formatted = {}
        if child.a is not None:
            formatted["href"] = child.a["href"]
            formatted["contents"] = "".join(map(str, child.a.contents))
            if fix_root and formatted["href"] == "#" and child.a.contents:
                slug = slugify.slugify(page_name) + ROOT_SUFFIX
                formatted["href"] = "#" + slug
            formatted["current"] = "current" in child.a.get("class", [])
        if child.ul is not None:
            formatted["children"] = ul_to_list(child.ul, fix_root, page_name)
        else:
            formatted["children"] = []
        out.append(formatted)
    return out


class CaptionList(list):
    _caption = ""

    def __init__(self):
        super().__init__()
        self._caption = ""

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, value):
        self._caption = value


def derender_toc(
    toc_text, fix_root=True, page_name: str = "md-page-root--link"
) -> List[dict]:
    try:
        toc = BeautifulSoup(toc_text, features="html.parser")
        nodes = CaptionList()
        for child in toc.children:
            if callable(child.isspace) and child.isspace():
                continue
            if child.name == "ul":
                nodes.extend(ul_to_list(child, fix_root, page_name))
            else:
                nodes.caption = "".join(map(str, child.contents))

        return nodes
    except Exception as exc:
        logger = logging.getLogger(__name__)
        logger.warning(
            "Failed to process toctree_text\n" + str(exc) + "\n" + str(toc_text)
        )
        return toc_text


def walk_contents(tags):
    out = []
    for tag in tags.contents:
        if hasattr(tag, "contents"):
            out.append(walk_contents(tag))
        else:
            out.append(str(tag))
    return "".join(out)


def table_fix(body_text, page_name="md-page-root--link"):
    # This is a hack to skip certain classes of tables
    ignore_table_classes = {"highlighttable", "longtable", "dataframe"}
    try:
        body = BeautifulSoup(body_text, features="html.parser")
        for table in body.select("table"):
            classes = set(table.get("class", tuple()))
            if classes.intersection(ignore_table_classes):
                continue
            del table["class"]
        first_h1 = body.find("h1")
        headers = body.find_all(re.compile("^h[1-6]$"))
        for i, header in enumerate(headers):
            for a in header.select("a"):
                if "headerlink" in a.get("class", ""):
                    header["id"] = a["href"][1:]
        if first_h1:
            slug = slugify.slugify(page_name) + ROOT_SUFFIX
            first_h1["id"] = slug
            for a in first_h1.select("a"):
                a["href"] = "#" + slug

        divs = body.find_all("div", {"class": "section"})
        for div in divs:
            div.unwrap()

        return str(body)
    except Exception as exc:
        logger = logging.getLogger(__name__)
        logger.warning("Failed to process body_text\n" + str(exc))
        return body_text


def get_html_context():
    return {"table_fix": table_fix, "derender_toc": derender_toc}
