About Pweave
-------------

Pweave is a scientific report generator and a literate programming
tool for Python. Pweave can capture the results and plots from data
analysis and works well with numpy, scipy and matplotlib. Pweave is
inspired by `Sweave
<http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_, an excellent tool
for R programmers, and the syntax is mostly compatible with it.   Pweave
supports reST, Sphinx, Latex, and Pandoc markdown markups.

Pweave uses `noweb <http://www.cs.tufts.edu/~nr/noweb/>`_ syntax for
separating code from documentation, but it also supports ERB style
evaluation of inline code.  Pweave is able to weave a python code
between ``<<>>=`` and ``@`` blocks and include the results and capture
`matplotlib <http://matplotlib.sourceforge.net/>`_ plots in the
document. Inline code in documentation chunks is marked using ``<%
%>`` (code will be evaluated in place) and ``<%= %>`` (result of
expression will be printed) tags. Pweave supports reST, Sphinx, Latex,
and Pandoc markdown markups.  . Pweave is good for creating reports
and tutorials. It can also be used to make websites together with
e.g. Sphinx or rest2web.

.. note:: 
   
   I've started `Pweave <https://groups.google.com/forum/?fromgroups=#!forum/pweave>`_ google group so you can
   ask for help and discuss new features. It will also be used to
   announce new releases.
   

Features:
----------

* **Execute python code** in the chunks and **capture** input and output to a report.
* **Use hidden code chunks,** i.e. code is executed, but not printed in the output file.
* Capture matplotlib graphics.
* Evaluate inline code in documentation chunks
* Cache all code and results from previous runs for fast report
  generation when you are only working with documentation. Inline code
  will be hidden in documentation mode.
* Supports reST, LaTeX, HTML or Pandoc markdown for document chunks
* Run from command line or interpreter.

Install and quickstart:
-----------------------

With easy_install:::

  easy_install -U Pweave

Or download the source package from `PyPi
<http://pypi.python.org/pypi/Pweave>`_ and run:::

  python setup.py install

Or run the binary exe installer on Windows.

After the installation you get options with:

::

  $ Pweave --help
  $ Ptangle

.. note:: Windows users: Check that the Python scripts directory is in
   your path (e.g. for me this c:\\python27\\scripts).



Documentation
-------------

Browse `documentation <docs.html>`_ or go straight to an `example
document <examples.html>`_


Thanks
------

Thanks to following people for contributing patches and ideas: Tamas
Nepusz, Nicky van Foreest, Mark Edgington, Thomas Unterthiner, Matthew McDonald.

