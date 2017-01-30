

Subclassing formatters
======================

.. currentmodule:: pweave

In the previous section we customized the output format by altering
the format dictionary. Sometimes more advanced customizations are
needed. This can be done by subclassing `Existing formatters <https://bitbucket.org/mpastell/pweave/src/eabf2f02b6af106241edb9bc4d7f6c9fc11f1eb2/pweave/formatters.py?at=release>`_
.

The base class PwebFormatter has a method :py:meth:`preformat_chunk` that
processes all chunks before they are processed by default formatters.

Suppose I have this `document <_static/ma.mdw>`_ (view the source in
browser) using markdown markup and I want convert the doc chunks to
HTML and output code chunks using Pweave default HTML formatter.

I can do this by subclassing :py:class:`PwebHTMLFormatter`. MDtoHTML class below
converts the content of all documentation chunks to HTML using python
`Markdown <https://pypi.python.org/pypi/Markdown>`_
package. (:py:attr:`chunk['type']` for code chunks is "code"). *The class also
stores the chunks for us to see what they contain, but that's not
needed for formatting.* 



.. code-block:: python

    from pweave import *
    import markdown
    
    class MDtoHTML(PwebHTMLFormatter):
    
        chunks = [] #Let's keep a copy of chunks
    
        def preformat_chunk(self, chunk):
            MDtoHTML.chunks.append(chunk.copy()) #Store the chunks
            if chunk['type'] == "doc":
                chunk['content'] = markdown.markdown(chunk['content'])
            return(chunk)
    



The specified subclass can then be used as formatter with
:py:class:`Pweb` class.


.. code-block:: python

    doc = Pweb('ma.mdw')
    doc.setformat(Formatter = MDtoHTML)
    doc.weave()
    

::

    Processing chunk 1 named None from line 22
    Processing chunk 2 named None from line 31
    Processing chunk 3 named None from line 42
    Pweaved ma.mdw to ma.html
    
    



And `here <_static/ma.html>`_ is the weaved document.

A closer look at the chunks
---------------------------

Remember that we kept a copy of the chunks in the previous example? As
you can see below the chunk is a dictionary that contains code, results
and all of the chunk options. You can manipulate all of these options
as we did to content in previous example to control how the chunk is
formatted in output.

.. note:: 

  You can your own options (key = value) to chunks and
  they will also appear in the chunk dictionary.

  
Let's see what the first code chunk contains:


.. code-block:: python

    import pprint
    pprint.pprint(MDtoHTML.chunks[1])
    

::

    {'caption': False,
     'codeend': '',
     'codestart': '',
     'complete': True,
     u'content': u'\nfrom pylab import *\nimport scipy.signal as
    signal\n#A function to plot frequency and phase response\ndef
    mfreqz(b,a=1):\n    w,h = signal.freqz(b,a)\n    h = abs(h)\n
    return(w/max(w), h)\n',
     'doctype': 'html',
     'echo': True,
     'engine': 'python',
     'evaluate': True,
     'extension': 'html',
     'f_env': None,
     'f_pos': 'htpb',
     'f_size': (8, 6),
     'f_spines': True,
     'fig': True,
     'figfmt': '.png',
     'figure': [],
     'include': True,
     'name': None,
     u'number': 1,
     'option_string': u'',
     'outputend': '',
     'outputstart': '',
     'result': '\n\n',
     'results': 'verbatim',
     'savedformats': ['.png'],
     u'start_line': 22,
     'term': False,
     'termend': '',
     'termstart': '',
     u'type': u'code',
     'width': '600',
     'wrap': True}
    
    



.. note:: 

  Pweb class also uses separate classes to parse and execute
  the document, but subclassing these is not currently documented and
  is hopefully not needed.


Dealing with LaTeX files
-------------------------


Here is another example to show how to preformat LaTeX files.

Some packages, such as `Exsheets
<https://www.ctan.org/pkg/exsheets>`_, have difficulty with handling
the verbatim environment of LaTeX. One way to work around this problem
is to write the content of each code chunc to a file, and then include
the file contents in the latex file with the `lstinputlisting` command
of latex.

Specifically, in the formatter below, we write the contents of each
code chunk to a file with the same name as the source file, add a
number to it, and store the file in the `chunks` directory. Then we
replace the contents of the chunck with the `lstinputlisting` command
so that latex reads the file. Since there is no further need for the
environments, we set them them to empty strings. Finally, we save the
weaved result in a ".tx" file, so that our source file remains
unharmed.


.. code-block:: python

    #!/usr/bin/python3
    import os

    from pweave import Pweb, PwebTexPweaveFormatter


    class ToFile(PwebTexPweaveFormatter):
        chunks = []

        def preformat_chunk(self, chunk):
            ToFile.chunks.append(chunk.copy())  # Store the chunks
            if chunk['type'] == 'code':
                source = os.path.splitext(self.source)[0]
                fname = "chunks/{}_{}.tex".format(source, chunk['number'])
                if chunk['term']:
                    with open(fname, "w") as f:
                        f.write(chunk['result'])
                    chunk['result'] = r"\lstinputlisting{"+fname+"}"
                else:
                    with open(fname, "w") as f:
                        f.write(chunk['content'])
                    chunk['content'] = r"\lstinputlisting{"+fname+"}"
            return(chunk)


    fname = "example"
    doc = Pweb(fname+r".tex",  format="texpweave", output=fname+r".tx")
    doc.setformat(Formatter=ToFile)
    doc.updateformat({
        "outputstart": "\n",
        "outputend": "\n",
        "codestart": "\n",
        "codeend": "\n",
        "termstart": "\n",
        "termend": "\n",
    }
    )
    doc.weave()

                
