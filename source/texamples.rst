
.. index:: LaTeX example

LaTeX example
-------------

This is a simple example of a Pweave file
(`ma-tex.texw <_static/ma-tex.texw>`_) that uses LaTeX as the
documentation markup. The file demonstrates basic usage of Pweave and
how it can easily be used to add dynamic figures and tables.

Processing the file with raw latex format:

:: 

   Pweave -f tex ma-tex.texw


Processing the output .tex file with pdflatex produces this `pdf <_static/ma-tex.pdf>`_

Processing the file with texminted format:

:: 

   Pweave -f texminted ma-tex.texw

And the resulting `pdf <_static/ma-tex_minted.pdf>`_. 



.. note:: You need to add ``\usepackage{graphicx}`` if you are
    including plots to document's preamble yourself and
    ``\usepackage{minted}`` if you are using minted.


Example Pweave document
~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ma-tex.texw

And as result we get the LaTex document `ma-tex.tex <_static/ma-tex.tex>`_ (shown below).  

LaTeX output
~~~~~~~~~~~~

.. literalinclude:: ma-tex.tex


