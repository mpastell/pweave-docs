
=====================
 Using pweave module
=====================

.. currentmodule:: pweave

Pweave can also be used as module from the Python interpreter. This
has some advantages over just using the scripts. First the execution
of the code will be faster because all modules all already
imported. It is also possible to fully
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
document `ma.mdw <_static/ma.mdw>`_. Notice that pweave prints out the
progress so in case of an error you can tell in which chunk it
occurred.

.. change default options for code chunks



.. code-block:: python

    import pweave
    # Weave a pandoc document with default options
    pweave.weave('ma.mdw', doctype = "pandoc")


::

    Processing chunk 1 named None from line 22
    

::

    Processing chunk 2 named None from line 31
    Processing chunk 3 named None from line 42
    

::

    Weaved ma.mdw to ma.md
    




.. code-block:: python

    # Extract the code
    pweave.tangle('ma.mdw')


::

    ---------------------------------------------------------------------------AttributeError
    Traceback (most recent call last)<ipython-input-5-d41c1a734f25> in
    <module>()
          1 # Extract the code
    ----> 2 pweave.tangle('ma.mdw')
    ~/anaconda3/lib/python3.6/site-
    packages/Pweave-0.30a1-py3.6.egg/pweave/__init__.py in tangle(file,
    informat)
         65     :param file: ``string`` the pweave document containing the
    code
         66     """
    ---> 67     doc = Pweb(file, kernel = None, informat = informat)
         68     doc.tangle()
         69
    ~/anaconda3/lib/python3.6/site-
    packages/Pweave-0.30a1-py3.6.egg/pweave/pweb.py in __init__(self,
    source, doctype, informat, kernel, output, figdir, mimetype)
         67         self.theme = "skeleton"
         68
    ---> 69         self.setformat(doctype)
         70         self.read(reader = informat)
         71
    ~/anaconda3/lib/python3.6/site-
    packages/Pweave-0.30a1-py3.6.egg/pweave/pweb.py in setformat(self,
    doctype, Formatter)
        148
        149         self.formatter = Formatter([],
    --> 150                                    kernel = self.kernel,
        151                                    language = self.language,
        152                                    mimetype =
    self.mimetype.type,
    AttributeError: 'Pweb' object has no attribute 'kernel'
    



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
