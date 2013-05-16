Changing defaults
_________________

Default chunk options are stored in `pweave.Pweb.defaultoptions`
dictionary. You can manipulate the dictionary to change the options.

**Have a look at current defaults:**


.. code-block:: python

    from pweave import *
    import pprint
    pprint.pprint(Pweb.defaultoptions)

::

    {'caption': False,
     'complete': True,
     'echo': True,
     'evaluate': True,
     'f_env': None,
     'f_pos': 'htpb',
     'f_size': (8, 6),
     'fig': True,
     'include': True,
     'name': None,
     'results': 'verbatim',
     'term': False,
     'wrap': False}
    



**Change wrapping off and default figure position to "h!"**


.. code-block:: python

    Pweb.defaultoptions.update({'wrap' : False, 'f_pos' : "h!"})
    #Updated options
    pprint.pprint(Pweb.defaultoptions)

::

    {'caption': False,
     'complete': True,
     'echo': True,
     'evaluate': True,
     'f_env': None,
     'f_pos': 'h!',
     'f_size': (8, 6),
     'fig': True,
     'include': True,
     'name': None,
     'results': 'verbatim',
     'term': False,
     'wrap': False}
    


