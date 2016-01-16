<HTML>
<HEAD>
<link rel="stylesheet" href="pygments.css"/>
</HEAD>
<BODY>
 

# Pweave Example - Frequency response of a moving average filter

[Matti Pastell](http://mpastell.com/)

Create 11 point moving average filter and plot its frequency response and print the values.


~~~~{.python}
from pylab import *
import scipy.signal as signal
#A function to plot frequency and phase response
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h = abs(h)
    return(w/max(w), h)
~~~~~~~~~~~~~



Make the impulse response function and use terminal formatted output.


~~~~{.python}
>>> n = 11.
>>> n
11.0
>>> b = repeat(1/n, n)
>>> b
array([ 0.09090909,  0.09090909,  0.09090909,  0.09090909,
0.09090909,
        0.09090909,  0.09090909,  0.09090909,  0.09090909,
0.09090909,
        0.09090909])

~~~~~~~~~~~~~



Calculate the frequency response and plot it:


~~~~{.python}
w, h = mfreqz(b)
#Plot the function
plot(w,h,'k')
ylabel('Amplitude')
xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
show()
~~~~~~~~~~~~~

![Frequency response of an 11 point moving average filter](figures/ma_figure3_1.pdf)



</BODY>
</HTML>

