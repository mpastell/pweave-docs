About Pweave
============

Pweave is a scientific report generator and a literate programming
tool for Python. Pweave can capture the results and plots from data
analysis and works well with numpy, scipy and matplotlib. Pweave is
inspired by `Sweave <http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_, an excellent tool
for R programmers, and the syntax is mostly compatible with it. Pweave
supports reST, Sphinx, Latex, and Pandoc markdown markups.

Pweave uses `noweb <http://www.cs.tufts.edu/~nr/noweb/>`_ syntax for
separating code from documentation, but it also supports ERB style
evaluation of inline code.  Pweave is able to weave a python code
between ``<<>>=`` and ``@`` blocks and include the results and capture
`matplotlib <http://matplotlib.sourceforge.net/>`_ plots in the
document. Inline code in documentation chunks is marked using ``<%
%>`` (code will be evaluated in place) and ``<%= %>`` (result of
expression will be printed) tags.

Pweave is good for creating reports, tutorials. presentations ect. with embedded python
code It can also be used to make websites together with e.g. Sphinx or rest2web.

.. note::

   Report bugs on `Github <https://github.com/mpastell/Pweave>`_.
   Post your questions and comments to `Pweave <https://groups.google.com/forum/?fromgroups=#!forum/pweave>`_
   google group.


Features:
---------

* Python 2.7 and 3.4 compatibility
* **Execute python code** in the chunks and **capture** input and output to a report.
* **Use hidden code chunks,** i.e. code is executed, but not printed in the output file.
* Capture matplotlib graphics.
* Evaluate inline code in documentation chunks
* Cache all code and results from previous runs for fast report
  generation when you are only working with documentation. Inline code
  will be hidden in documentation mode.
* Supports reST, LaTeX, HTML or markdown for document chunks
* Publish reports from Python scipts. Similar to R markdown.
* Run from command line or interpreter.
* Support also for Octave, Matlab and Julia code.

Install and quickstart:
-----------------------

with pip::

  pip install --upgrade Pweave

with conda::

  conda install -c https://conda.binstar.org/mpastell pweave

Or download the source package from `PyPi
<http://pypi.python.org/pypi/Pweave>`_ and run::

  python setup.py install


After the installation you get options with:

::

  $ pweave --help
  $ ptangle


Documentation
-------------

Browse `documentation <docs.html>`_ or go straight to an `examples <examples/index.html>`_


Thanks
------

Thanks to following people for contributing patches and ideas: Tamas
Nepusz, Nicky van Foreest, Mark Edgington, Thomas Unterthiner, Matthew
McDonald, Grant Goodyear, Aaron O'Leary.
