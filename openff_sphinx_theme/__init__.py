"""OpenFF Sphinx theme."""

import hashlib
import inspect
import os
import sys
from pathlib import Path
from multiprocessing import Manager
from typing import List, Optional
from xml.etree import ElementTree

import bs4
import slugify
from bs4 import BeautifulSoup
from sphinx.util import console, logging
import sass

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

ROOT_SUFFIX = "--page-root"


def setup(app):
    """Setup connects events to the sitemap builder"""
    app.connect("html-page-context", add_html_link)
    app.connect("build-finished", create_sitemap)
    app.connect("build-finished", reformat_pages)
    app.connect("build-finished", compile_css)
    app.connect("build-finished", minify_css)
    app.connect("builder-inited", register_template_functions)
    manager = Manager()
    site_pages = manager.list()
    sitemap_links = manager.list()
    app.multiprocess_manager = manager
    app.sitemap_links = sitemap_links
    app.site_pages = site_pages
    app.add_html_theme(
        "openff_sphinx_theme", os.path.join(html_theme_path()[0], "openff_sphinx_theme")
    )
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def compile_css(app, exception):
    """Compile Bulma SASS into CSS"""
    if exception is not None:
        return

    theme_path = Path(html_theme_path()[0]) / "openff_sphinx_theme"
    src = theme_path / "sass/site.sass"
    dest = Path(app.outdir) / "_static/site.css"

    accent_color = app.config["html_theme_options"].get(
        "color_accent", "openff-toolkit-blue"
    )
    accent_color = {
        "openff-blue": "#015480",
        "openff-toolkit-blue": "#2F9ED2",
        "openff-yellow": "#F08521",
        "openff-orange": "#F03A21",
        "aquamarine": "#2CDA9D",
        "lilac": "#E4B7E5",
        "amaranth": "#A40E4C",
        "grape": "#AB92BF",
        "violet": "#8D6B94",
        "pink": "#EE4266",
        "pale-green": "#EE4266",
        "green": "#04E762",
        "crimson": "#D62839",
        "eggplant": "#754F5B",
        "turquoise": "#2DE1C2",
    }.get(accent_color, accent_color)

    if app.config["html_theme_options"].get("css_minify", False):
        output_style = "compressed"
    else:
        output_style = "expanded"

    css = sass.compile(
        filename=str(src),
        output_style=output_style,
        custom_functions={"accent_color": lambda: accent_color},
    )

    print(f"Writing compiled SASS to {console.colorize('blue', str(dest))}")

    with open(dest, "w") as f:
        print(css, file=f)


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

    root = ElementTree.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ElementTree.SubElement(root, "url")
        ElementTree.SubElement(url, "loc").text = link
    app.sitemap_links[:] = []

    ElementTree.ElementTree(root).write(filename)


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


def register_template_functions(app):
    config = app.config
    config.html_context = {**get_html_context(), **config.html_context}


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

    def __init__(self, caption=""):
        super().__init__()
        self._caption = caption

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, value):
        self._caption = value


def derender_toc(
    toc_text, fix_root=True, page_name: str = "md-page-root--link"
) -> List[dict]:
    nodes = []
    try:
        toc = BeautifulSoup(toc_text, features="html.parser")
        for child in toc.children:
            if callable(child.isspace) and child.isspace():
                continue
            if child.name == "p":
                nodes.append({"caption": "".join(map(str, child.contents))})
            elif child.name == "ul":
                nodes.extend(ul_to_list(child, fix_root, page_name))
            else:
                raise NotImplementedError
    except Exception as exc:
        logger = logging.getLogger(__name__)
        logger.warning(
            "Failed to process toctree_text\n" + str(exc) + "\n" + str(toc_text)
        )

    return nodes


# These final lines exist to give sphinx a stable str representation of
# this function across runs, and to ensure that the str changes
# if the source does.
derender_toc_src = inspect.getsource(derender_toc)
derender_toc_hash = hashlib.sha512(derender_toc_src.encode()).hexdigest()


class DerenderTocMeta(type):
    def __repr__(self):
        return f"derender_toc, hash: {derender_toc_hash}"

    def __str__(self):
        return f"derender_toc, hash: {derender_toc_hash}"


class DerenderToc(object, metaclass=DerenderTocMeta):
    def __new__(cls, *args, **kwargs):
        return derender_toc(*args, **kwargs)


def get_html_context():
    return {"derender_toc": DerenderToc}
