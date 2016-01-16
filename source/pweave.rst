
=====================
 Using pweave module
=====================

.. currentmodule:: pweave

Pweave can also be used as module from the Python interpreter. This
has some advantages over just using the scripts. First the execution
of the code will be faster because all modules all already
imported. Second you can work interactively with the data after the
code from the document has been run. Further it is possible to fully
customize the document execution and formatting using the :py:class:`Pweb` class.

pweave module contains two functions :py:func:`weave` and
:py:func:`tangle` that offer the same functionality as the command
line scripts.

.. note:: 

  This document was also created with Pweave, have a look at the
  `source <_static/pweave.rstw>`_.


Simple weaving and tangling:
============================

Here's and example of simple weaving and tangling using example
document `ma.Pnw <_static/ma.Pnw>`_. Notice that pweave prints out the
progress so in case of an error you can tell in which chunk it
occurred. Also in case of an error returns already evaluated results
from the documents namespace :py:attr:`PwebProcessorGlobals.globals` to global namespace.

.. change default options for code chunks
 


.. code-block:: python

    >>> import pweave
    >>> # Weave a document with default options
    >>> pweave.weave('ma.Pnw')
    Traceback (most recent call last):
      File "< chunk 1 named None in pweave.rstw >", line 1, in <module>
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/__init__.py", line 69, in
    weave
        doc.weave(shell)
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/pweb.py", line 140, in weave
        self.parse()
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/pweb.py", line 93, in parse
        parser = self.Reader(file=self.source)
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/readers.py", line 21, in
    __init__
        codefile = io.open(self.source, 'r', encoding='utf-8')
    IOError: [Errno 2] No such file or directory: 'ma.Pnw'
    >>> # Extract the code
    >>> pweave.tangle('ma.Pnw')
    Traceback (most recent call last):
      File "< chunk 1 named None in pweave.rstw >", line 1, in <module>
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/__init__.py", line 96, in
    tangle
        doc.tangle()
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/pweb.py", line 147, in tangle
        self.parse()
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/pweb.py", line 93, in parse
        parser = self.Reader(file=self.source)
      File "/usr/local/lib/python2.7/dist-
    packages/Pweave-0.23.2-py2.7.egg/pweave/readers.py", line 21, in
    __init__
        codefile = io.open(self.source, 'r', encoding='utf-8')
    IOError: [Errno 2] No such file or directory: 'ma.Pnw'
    
    



Pweave function reference
--------------------------

.. autofunction:: pweave.weave

.. autofunction:: pweave.tangle

.. autofunction:: pweave.publish

.. autofunction:: pweave.convert

.. autofunction:: pweave.spin


More options with Pweb Class
============================

Weaving, tangling and pweave options are implemented using
:py:class:`Pweb` class. There is an `example <customizing.html>`_
about customizations and the class reference is below.

Pweb Class
----------

.. autoclass:: pweave.Pweb
   :members: 


   
