#!/bin/bash

#Weave docs
cd pweave_source
pweave -f sphinx pweave.rstw
pweave -f sphinx formats.rstw
pweave -f sphinx customizing.rstw
pweave -f sphinx defaults.rstw
pweave -f sphinx subclassing.rstw

cp *.rstw ../source/_static #copy Pweave documents to _static
mv  *.rst ../source #copy Pweave documents to _static
cp *.Pnw ../source/_static
cp ma.mdw ../source/_static #Weaved in subclassing.rst
cp -r figures ../source/_static
cp -r figures ../build/latex
cp -r figures ../build/html
mv ma.html ../source/_static
cd ..

#Example gallery
cd examples
make
cd ..
cp examples/* source/examples
