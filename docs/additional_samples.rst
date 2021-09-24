==========================
``Additional`` ``Samples``
==========================


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

    <span style="font-size: 2rem;" class="md-icon">&#xe869;</span>

translates to a the site's icon:

.. raw:: html

    <span style="font-size: 2rem;" class="md-icon">&#xe869;</span>

The material icon font provides hundreds to choose from. You can use the ``<i>`` tag or the
``<span>`` tag.

.. raw:: html

    <i style="font-size: 1rem;" class="md-icon">&#xe158;</i>
    <i style="font-size: 1.2rem;" class="md-icon">&#xe155;</i>
    <i style="font-size: 1.4rem;" class="md-icon">&#xe195;</i>
    <i style="font-size: 1.6rem;" class="md-icon">&#xe255;</i>
    <i style="font-size: 1.8rem;" class="md-icon">&#xe3c9;</i>
    <i style="font-size: 2.0rem;" class="md-icon">&#xe811;</i>
    <i style="font-size: 2.2rem;" class="md-icon">&#xe812;</i>
    <i style="font-size: 2.4rem;" class="md-icon">&#xe813;</i>
    <i style="font-size: 2.6rem;" class="md-icon">&#xe814;</i>
    <i style="font-size: 2.8rem;" class="md-icon">&#xe815;</i>


Tables
======
Here are some examples of Sphinx
`tables <http://www.sphinx-doc.org/rest.html#rst-tables>`_. The Sphinx Material
all classes and only applies the default style to classless tables. If you want
to use a custom table class, you will need to do two thing. First, apply it
using ``.. cssclass:: custom-class`` and then add it to your configuration's
``table_classes`` variable.

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

User-styled Table
-----------------

.. note::

   `table_classes` is set to `["plain"]` in the site's configuration. Only plain
   remains as the class of the table. Other standard classes applied by Sphinx are
   removed.

   This is feature demonstration. There is no css for the plain class, and so
   this is completely unstyled.

.. cssclass:: plain

=====  ======  =======
User   Styled  Table
=====  ======  =======
cell1  cell2   cell3
...    ...     ...
...    ...     ...
=====  ======  =======

List Tables
-----------

.. list-table:: A List Table
   :header-rows: 1

   * - Column 1
     - Column 2
   * - Item 1
     - Item 2

Alignment
~~~~~~~~~

.. warning:: Alignment is not currently working as expected.

.. list-table:: Center Aligned
   :header-rows: 1
   :align: center

   * - Column 1
     - Column 2
   * - Item 1
     - Item 2


.. list-table:: Right Aligned
   :widths: 15 10 30
   :header-rows: 1
   :align: right

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out
   * - Gannet Ripple
     - 1.99
     - On a stick!

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

Glossaries
==========

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

Math
====

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2


.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

Production Lists
================

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`
