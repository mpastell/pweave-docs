
# Using Octave with Pweave

You can also use Pweave to publish reports using GNU Octave or Matlab. The
was  released with Pweave 0.23.

**Features:**

* Inline code and noweb style chunks
* Capturing of figures

**Limitations**

* No terminal chunks
* Only one figure/chunk

You can use inline code chunks like in Python documents:

Give y value 300  in hidden chunk.

And let's verify that it worked:


~~~~{.octave}
y
~~~~~~~~~~~~~

~~~~{.octave}
y =  300

~~~~~~~~~~~~~



You can also display the result from inline chunk 2+5= 7

## Solving least squares


and trying out plotting features:


~~~~{.octave}
x = (0:25) + randn(1, 26);
y = linspace(0, 5, length(x));
a = x' \ y'
plot(x , y, 'o')
hold on
plot(x, a*x, 'r')
hold off
figure()
hist(a*x - y)
title('Histogram of residuals')
~~~~~~~~~~~~~

~~~~{.octave}
a =  0.20284

~~~~~~~~~~~~~

![](figures/octave_sample_figure2_.png)\


And include a plot but hide the code:


![Sinc function](figures/octave_sample_figure3_.png)

