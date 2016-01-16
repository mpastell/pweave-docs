
Publishing scipts
=================

As option to using the noweb format Pweave can also publish html and pdf
documents from Python scripts with a specific format.

These scripts can be executed normally using Python or published to HTML with Pweave Text is written in markdown in lines starting with "#' " and code is executed and results are included in the published document. The concept is similar to publishing documents with MATLAB or using Knitr's `spin <http://yihui.name/knitr/demo/stitch/>`__.

Notice that you don't need to define chunk options (see Pweave docs ), but you do need one line of whitespace between text and code. If you want to define options you can do it on using a line starting with #+. just before code e.g. #+ term=True, caption='Fancy plots.'. See the example below for the markup.

The scripts can be published using the `pypublish` scipts:

:download:`FIR_design.py <examples/FIR_design.py>`, :download:`FIR_design.html <examples/FIR_design.html>` , :download:`FIR_design.pdf <examples/FIR_design.pdf>` .

.. code:: shell

    pypublish FIR_design.py
    pypublish -f pdf FIR_design.py
