
Customizing output
==================

.. index:: customizing

.. currentmodule:: pweave

Pweave has several output formats and you can customize the output
with chunk options. However you may want to customize the output for
different purposes.

The simplest form of customization is to update the *format dictionary*
of an existing format. It sets chunk delimiters, output extension and
figure format and width.

You can do this easily with :py:class:`Pweb` class. Below
is a small demonstration using ReST Pweave document `ma2.Pnw <_static/ma2.Pnw>`_.

Let's start by creating an instance of :py:class:`Pweb` class with rst document:


.. code-block:: python

    >>> from pweave import *
    >>> from pprint import pprint
    >>> doc = Pweb('ma2.Pnw', format = "rst")
    
    



Have a look at what the format dictionary contains:


.. code-block:: python

    >>> pprint(doc.getformat())
    {'codeend': '\n\n',
     'codestart': '.. code:: %s\n',
     'doctype': 'rst',
     'extension': 'rst',
     'figfmt': '.png',
     'indent': '    ',
     'outputend': '\n\n',
     'outputstart': '.. code::\n',
     'savedformats': ['.png'],
     'termend': '\n\n',
     'termindent': '    ',
     'termstart': '.. code:: %s\n',
     'width': '15 cm'}
    
    



The names of the dictionary elements are hopefully self
explanatory. You'll notice that you can specify start and end tag for
code, results and term as well as block indent.

You can change the formats using :py:meth:`Pweb.updateformat` method. Let's set the
default figure width to 10cm and figure format to pdf. The
:py:attr:`savedformats` key allows you to specify multiple formats to save and
:py:attr:`figfmt` specifies what format is used in the output.


.. code-block:: python

    >>> doc.updateformat({'width' : '10cm', 'figfmt' : '.pdf',
    'savedformats' : ['.pdf']})
    
    



And after setting options weave and tangle the document:


.. code-block:: python

    >>> doc.weave()
    Traceback (most recent call last):
      File "< chunk 4 named None in customizing.rstw >", line 1, in
    <module>
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
    IOError: [Errno 2] No such file or directory: 'ma2.Pnw'
    >>> doc.tangle()
    Traceback (most recent call last):
      File "< chunk 4 named None in customizing.rstw >", line 1, in
    <module>
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
    IOError: [Errno 2] No such file or directory: 'ma2.Pnw'
    
    



View this page as `Pweave document <_static/customizing.rstw>`_ .
