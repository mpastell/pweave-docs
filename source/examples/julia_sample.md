
# Using Julia with Pweave

This a sample [Julia](http://julialang.org/) noweb document that can be
executed using Pweave. Output from code chunks and Winston plots will be included in the
weaved document. 

You can execute this document (<https://github.com/mpastell/Pweave/tree/master/examples/julia_sample.mdw>) 
using:

    pweave -f pandoc -s julia julia_sample.mdw

**Known limitations:**

Most of the features and chunk options from Pweave Python (see
<http://mpastell.com/pweave/>) version work with Julia too, but there
are a few known limitations:

* Terminal chunks are not implemented.
* You can only capture one plot/chunk and you need Fig=True for those
  chunks (it is false by default).



~~~~{.python}
using Winston
~~~~~~~~~~~~~

~~~~{.python}
<type 'exceptions.SyntaxError'>
invalid syntax (chunk, line 2)
~~~~~~~~~~~~~



You can use hidden inline chunks: . Or include the results
from inline expressions: 2+3=5. 

Variable p was declared in a hidden inline chunk:


~~~~{.python}
println(p)
~~~~~~~~~~~~~

~~~~{.python}
<type 'exceptions.NameError'>
name 'println' is not defined
~~~~~~~~~~~~~



Here is a captured plot:


~~~~{.python}
t = linspace(0, 2*pi, 100)
plot(t, sinc(t))
xlabel("x")
ylabel("sinc(x)")
~~~~~~~~~~~~~

~~~~{.python}
<type 'exceptions.NameError'>
name 'linspace' is not defined
~~~~~~~~~~~~~



You can also include a plot with caption and hide the code:


~~~~{.python}
<type 'exceptions.NameError'>
name 'plot' is not defined
~~~~~~~~~~~~~


