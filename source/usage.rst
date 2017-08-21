
Pweave Basics
=============

.. index:: source document, output document

Pweave documents
________________

A Pweave input document contains documentation and code separated with special
markup. Pweave supports several input formats for different purposes. All of the
source formats produce identical output for code. You need to tell the input format
to Pweave using `-i` command line option.

Code chunk formats
------------------

markdown
++++++++

Pweave can run code from fenced markdown python code blocks. All of the
following are valid ways to define a code chunk:

::

  ```python
  ```{python}
  ```{.python}

..

However options can only be defined in brackets:

::

  ```{python, caption = "Some figure"}


noweb
+++++

Noweb syntax for defining code chunks has been adopted from  `Sweave
<http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_.


Code chunk starts with a line marked with ``<<>>=`` or ``<<options>>=`` and end
with line marked with ``@``. The code between the start and end markers
is executed and the output is captured to the output document.

**Example:** A code chunk that saves and displays a 12 cm wide image
and hides the source code:

::

  <<fig = True, width = '12 cm', echo = False>>=
  from pylab import *
  plot(arange(10))
  show()
  @



Documentation chunk
-------------------

 The rest of the document is just copied to ouput and can be written with
 several different markup languages. See `formats <formats.html>`_ page for
 a list of supported output formats.

Inline code
-----------

 Pweave supports evaluating inline code in documentation chunks
 using ``<% %>`` (code will be evaluated in place) and ``<%= %>``
 (result of expression will be printed) tags. Inline code will not
 be included in weaved document.

.. versionadded:: 0.2

.. index:: options, figures, inline code chunks

Weaving Pweave Documents
________________________

Weaving a Pweave source file produces a document
that contains text and the weaved code together with its
evaluated output.  All of the produced figures are placed in the
'figures/' folder as a default.


**Pweave documents are weaved from the shell with the command:**

.. describe:: pweave [options] sourcefile

  Options:
    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -f DOCTYPE, --format=DOCTYPE
                          The output format. Available formats:  tex, texminted,
                          texpweave, texpygments, rst, pandoc, markdown,
                          leanpub, sphinx, html, md2html, softcover,
                          pandoc2latex, pandoc2html, notebook Use Pweave -l to
                          list descriptions or see
                          http://mpastell.com/pweave/formats.html
    -i INFORMAT, --input-format=INFORMAT
                          Input format: noweb, markdown, notebook or script
    -k KERNEL, --kernel=KERNEL
                          Jupyter kernel used to run code: default is python3
    -o OUTPUT, --output=OUTPUT
                          Name of the output file
    -l, --list-formats    List output formats
    -m, --matplotlib      Disable matplotlib
    -d, --documentation-mode
                          Use documentation mode, chunk code and results will be
                          loaded from cache and inline code will be hidden
    -c, --cache-results   Cache results to disk for documentation mode
    -F FIGDIR, --figure-directory=FIGDIR
                          Directory path for matplolib graphics: Default
                          'figures'
    --cache-directory=CACHEDIR
                          Directory path for cached results used in
                          documentation mode: Default 'cache'
    -g FIGFORMAT, --figure-format=FIGFORMAT
                          Figure format for matplotlib graphics: Defaults to
                          'png' for rst and Sphinx html documents and 'pdf' for
                          tex
    -t MIMETYPE, --mimetype=MIMETYPE
                          Source document's text mimetype. This is used to set
                          cell type in Jupyter notebooks


Weave a markdown document. Output format is detected based on extension,
but in can be changed using the ```-f`` option:

::

  $ pweave FIR_design.pmd



Get options:

::

  $ pweave --help


Tangling Pweave Documents
_________________________

Tangling refers to extracting the source code from Pweave
document. This can be done using Ptangle script::

  $ ptangle file

  $ ptangle ma.pnw
  Tangled code from ma.pnw to ma.py

Caching results
_______________

Pweave has documentation mode (invoked with ``-d``) that caches code
and all results from code chunks so you don't need to rerun the code
when you are only working on documentation. You can cache the results
using the `-c` option, if there are no cached results then
documentation mode will create the cache on first run.  Inline code
chunks will be hidden in documentation mode. Additionally Pweave will
warn you if the code in cached chunks has changed after the last run.


Document types
______________

.. describe:: Source document

   Contains a mixture of documentation and code chunks. Pweave will
   evaluate the code and leave the documentation chunks as they
   are. The documentation chunks can be written either with reST,Latex
   or Pandoc markdown. The source document is processed using
   *Pweave*, which gives us the formatted output document.

.. describe:: Weaved document

   Is produced by Pweave from the source document. Contains the
   documentation, original code, the captured outputof the code and
   optionally captured `matplotlib
   <http://matplotlib.sourceforge.net/>`_ figures.

.. describe:: Source code

   Is produced by Pweave from the source document. Contains the source
   code extracted from the code chunks.

.. index::  syntax, code chunk, documentation chunk
