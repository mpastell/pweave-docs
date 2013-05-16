
Pweave Basics
=============

.. index:: source document, output document


Pweave syntax
_____________

Pweave uses noweb syntax for defining the code chunks and
documentation chunks, just like `Sweave
<http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_.

.. describe:: Code chunk

   start with a line marked with ``<<>>=`` or ``<<options>>=`` and end
   with line marked with ``@``. The code between the start and end markers
   is executed and the output is captured to the output document. See
   for options below.

   **Example:** A code chunk that saves and displays a 12 cm wide image
   and hides the source code:

::

  <<fig = True, width = '12 cm', echo = False>>=
  from pylab import *
  plot(arange(10))
  show()
  @

.. describe:: Documentation chunk

   Are the rest of the document (between ``@`` and ``<<>>=`` lines and the
   first chunk be default) and can be written with several different
   markup languages.

.. describe:: Inline code

   Pweave supports evaluating inline code in documentation chunks
   using ``<% %>`` (code will be evaluated in place) and ``<%= %>``
   (result of expression will be printed) tags. Inline code will not
   be included in weaved document.

   **Example**: Use inline code to set some matplotlib options.

::

   <%
   import matplotlib
   matplotlib.rcParams.update({'figure.figsize' : (6, 4),
                           'savefig.dpi': 100,
                           'font.size' : 10 })
   %>


.. versionadded:: 0.2

.. index:: options, figures, inline code chunks





Weaving Pweave Documents
________________________

Weaving a Pweave source file produces a document
that contains text and the weaved code together with its
evaluated output.  All of the produced figures are placed in the
'figures/' folder as a default. 

See `formats <formats.html>`_ page for a list of supported
output formats.

**Pweave documents are weaved from the shell with the command:**

.. describe:: Pweave [options] sourcefile

Options:

.. program:: Pweave

.. cmdoption:: --version

   show the version number and exit

.. cmdoption:: -h, --help

   show help message and exit

.. cmdoption:: -f FORMAT, --format FORMAT

   The output format. Available formats: sphinx, pandoc, tex, html,
   rst, texpweave, texminted. See `<http://mpastell.com/pweave/formats.html>`_


.. cmdoption::  -m MPLOTLIB, --matplotlib=MPLOTLIB

   Do you want to use matplotlib (or Sho with Ironpython) true
   (default) or false

.. cmdoption::  -d, --documentation-mode

   Use documentation mode, chunk code and results will be loaded from
   cache and inline code will be hidden

.. cmdoption::  -c, --cache-results

   Cache results to disk for documentation mode

.. cmdoption::  --figure-directory=FIGDIR

   Directory path for matplolib graphics: Default 'figures'

.. cmdoption::  --cache-directory=CACHEDIR

   Directory path for cached results used in documentation mode:
   Default 'cache'

.. cmdoption::  -g FIGFMT, --figure-format=FIGFMT

   Figure format for matplolib graphics: Defaults to 'png' for rst and
   Sphinx html documents and 'pdf' for tex

Weave a document with default options (rst with png figures)

::

  $ Pweave ma.Pnw
  Output written to ma.rst


Weave a Latex document with png figures:

::

  $ Pweave -f tex -g png source.Pnw

Get options:

::

  $ Pweave --help


Tangling Pweave Documents
_________________________

Tangling refers to extracting the source code from Pweave
document. This can be done using Ptangle script::

  $ Ptangle file

  $ Ptangle ma.pnw
  Tangled code from ma.pnw to ma.py



Code Chunk Options
__________________

Pweave currently has the following options for processing the code
chunks.

.. envvar:: name, label

   If the first option of chunk is unnamed it will become the chunk
   name, you can also set the chunk name using the name or label (*for
   Sweave compatibility*) keys. All of these definitions are equal
   ``<<analysis, Fig = True>>=``,  ``<<Fig = True, name =
   'analysis'>>=``,  ``<<Fig = True, label = 'analysis'>>=``. Chunk
   names are used for figure names, but expanding named chunks in the
   Pweave todo list.

.. versionadded:: 0.2

.. envvar:: fig = True or (False)

   Whether a matplotlib plot produced by the code chunk should be
   included in the file. The figure will be added with '.. image::'
   directive in .rst and \\includegraphics tag in .tex documents. See
   the 'caption' option if you want to use figure environment. As of
   version 0.21 Pweave supports multiple figures per code chunk.


.. envvar:: include = True or (False)
   
   If include is True generated figures are automatically included in
    the document otherwise figures are generated, but not
    included. This is useful if you want more control over figure
    formatting e.g. use subfigures in Latex.  
   
.. versionadded:: 0.21

.. envvar:: width

   The width of the created figure (using format specific
   markup). The default width depends on the otuput format.

.. envvar:: echo = True or (False)

   Echo the python code in the output document. If False the source
   code will be hidden.

.. envvar:: evaluate = True or (False).

   Evaluate the code chunk. If False the chunk won't be executed.

.. envvar:: results = 'verbatim'

   The output format of the printed results. 'verbatim' for literal
   block, 'hidden' for hidden results or anything other string for raw
   output (I tend to use 'tex' for Latex and 'rst' for rest. Raw output
   is useful if you wan't to e.g. create tables from code chunks.

.. envvar:: caption = ''

   A string providing a caption for the figure produced in the code
   chunk. Can only be used with 'fig = True' option. If a caption is
   provided the figure will be added in the .rst document with the
   '.. figure::' directive and as a figure float in Latex.

.. versionadded:: 0.12

.. envvar:: term = False or (True)

   If True the output emulates a terminal session i.e. the code chunk
   and the output will be printed as a `doctest block
   <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#doctest-blocks>`_. Can
   also be used in latex documents, where the output will formatted as
   verbatim.

.. envvar:: f_pos = "htpb"

   Sets the figure position for latex figures.

.. versionadded:: 0.21

.. envvar:: wrap = True or (False,"code", "results")

   Controls wrapping of long lines. If True both code and output are
   wrapped to 75 characters. You can also specify "code" or "results" options to
   wrap only input or output.

.. versionadded:: 0.21

.. note::

   You can now use loops, if sentences and function definitions in
   term chunks (as of Pweave 0.13). However sometimes execution in
   term mode can fail in which case the chunk will be executed with
   term=False.

.. versionadded:: 0.12

.. include:: defaults.rst


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
