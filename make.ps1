
#Write-Host $args.length
#Write-Host $args[0]

if ($args.length -eq 0){$arg = "docs"}
else {$arg = $args[0]}

#Write-Host "Ru"$arg

if ($arg -eq "pweave" -or $arg -eq "all")
{
    #Build Pweave
    cd ..\pweave
    python setup.py install
    cd ..\pweave-docs
}


if ($arg -eq "docs" -or $arg -eq "all")
{
    #Weave docs
    cd pweave_source
    pweave -f sphinx pweave.rstw
    pweave -f sphinx formats.rstw
    pweave -f sphinx customizing.rstw
    pweave -f sphinx defaults.rstw
    pweave -f sphinx subclassing.rstw

    cp -Force *.rstw ..\source\_static #copy Pweave documents to _static
    mv -Force *.rst ..\source #copy Pweave documents to _static
    cp -Force *.Pnw ..\source\_static
    cp -Force ma.mdw ..\source\_static #Weaved in subclassing.rst
    cp -Force -Recurse figures ..\source\_static
    cp -Force -Recurse figures ..\build\latex
    cp -Force -Recurse figures ..\build\html
    mv -Force ma.html ..\source\_static
    cd ..
}

#Weave examples
if ($arg -eq "ex" -or $arg -eq "all")
{
  cd examples
  pdf ma.rstw
  pweave -f sphinx --figure-directory=_static ma.Pnw
  cp -Force *.Pnw ..\source\_static

  pweave -f tex ma-tex.texw
  pdflatex --shell-escape ma-tex.tex
  mv -Force ma.pdf ..\source\_static
  mv -Force ma-tex.pdf ..\source\_static

  pweave -f texminted ma-tex.texw
  pdflatex --shell-escape ma-tex.tex
  mv -Force ma-tex.pdf ..\source\_static\ma-tex_minted.pdf
  cp -Force ma-tex.tex ..\source\_static
  cp -Force ma-tex.tex ..\source\
  cp -Force ma-tex.texw ..\source\


  cp -Force -Recurse figures ..\source\_static
  cd ..
}

#Docs
if ($arg -eq "docs" -or $arg -eq "all")
{    
    #.\make.bat latex
    #cd build\latex
    #cd ..
    #cd ..
    #make
    #cp -Force build\latex\pweave-docs.pdf source\_static
    .\make.bat html
}
