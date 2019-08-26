==================
Additional Samples
==================


Various examples of styling applied to Sphinx constructs. You can
view the `source <./_sources/examples.txt>`_ of this page to see the specific
reStructuredText used to create these examples.

Subpages
========

Suppages get bread crumbs when they are not at the top level.

.. toctree::

    subpage/index



Headings
========
This is a first level heading (``h1``).

Sub-Heading
-----------
This is a second level heading (``h2``).

Sub-Sub-Heading
~~~~~~~~~~~~~~~
This is a third level heading (``h3``).


Code
====
The theme uses pygments for ``inline code text`` and
::

    multiline
    code text

Here's an included example with line numbers.

.. literalinclude:: ../sphinx_material/__init__.py
   :linenos:

It also works with existing Sphinx highlighting:

.. code-block:: html

    <html>
      <body>Hello World</body>
    </html>

.. code-block:: python

    def hello():
        """Greet."""
        return "Hello World"

.. code-block:: javascript

    /**
     * Greet.
     */
    function hello(): {
      return "Hello World";
    }


Admonitions
===========
The theme uses the ``admonition`` classes for Sphinx admonitions.

Note
----
.. note:: This is a **note**.

Todo
----

.. todo::

   It is essential to complete **todo** items.

Warning
-------
.. warning:: This is a **warning**.

Danger
------
.. danger:: This is **danger**-ous.

Attention
---------
.. attention:: Do I have your **attention**?

Caution
-------
.. caution:: Use **caution**!

Error
-----
.. error:: You have made a grave **error**.

Hint
----
.. hint:: Can you take a **hint**?

Important
---------
.. important:: It is **important** to correctly use admonitions.

Tip
---
.. tip:: Please **tip** your waiter.

Custom Admonitions
------------------
.. admonition:: Custom

   You can create your own admonitions with the default style.

Footnotes
=========
I have footnoted a first item [#f1]_ and second item [#f2]_.
This also references the second item [#f2]_.

.. rubric:: Footnotes
.. [#f1] My first footnote.
.. [#f2] My second footnote.

Icons
=====
The following template HTML:

.. code-block:: html

    <span style="font-size: 2rem;" class="md-icon">&#xe869</span>

translates to a the site's icon:

.. raw:: html

    <span style="font-size: 2rem;" class="md-icon">&#xe869</span>

The material icon font provides hundreds to choose from. You can use the ``<i>`` tag or the
``<span>`` tag.

.. raw:: html

    <i style="font-size: 1rem;" class="md-icon">&#xe158</i>
    <i style="font-size: 1.2rem;" class="md-icon">&#xe155</i>
    <i style="font-size: 1.4rem;" class="md-icon">&#xe195</i>
    <i style="font-size: 1.6rem;" class="md-icon">&#xe255</i>
    <i style="font-size: 1.8rem;" class="md-icon">&#xe3c9</i>
    <i style="font-size: 2.0rem;" class="md-icon">&#xe811</i>
    <i style="font-size: 2.2rem;" class="md-icon">&#xe812</i>
    <i style="font-size: 2.4rem;" class="md-icon">&#xe813</i>
    <i style="font-size: 2.6rem;" class="md-icon">&#xe814</i>
    <i style="font-size: 2.8rem;" class="md-icon">&#xe815</i>


Tables
======
Here are some examples of Sphinx
`tables <http://sphinx-doc.org/rest.html#rst-tables>`_. The Sphinx Bootstrap
Theme removes all Sphinx ``docutils`` classes and replaces them with the
default Bootstrap ``table`` class.  You can add additional table classes
using the Sphinx ``cssclass::`` directive, as demonstrated in the following
tables.

Grid
----
A grid table:


+------------------------+------------+----------+----------+
| Header1                | Header2    | Header3  | Header4  |
+========================+============+==========+==========+
| row1, cell1            | cell2      | cell3    | cell4    |
+------------------------+------------+----------+----------+
| row2 ...               | ...        | ...      |          |
+------------------------+------------+----------+----------+
| ...                    | ...        | ...      |          |
+------------------------+------------+----------+----------+


Simple
------
A simple table:

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======


Code Documentation
==================

An example Python function.

.. py:function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings

An example JavaScript function.

.. js:class:: MyAnimal(name[, age])

   :param string name: The name of the animal
   :param number age: an optional age for the animal
