# Primeira versão usável do DIMduct 2018.
Funciona em sistemas Windows (testados 10 e 8), mas é bem pesado e demora pra iniciar a primeira vez. Também o manual não está de acordo.

Pasta *python/* está compactada pra poder fazer upload, se for usar tem que descompactar.

## Sobre os *DIMduct.cpp* e *DIMduct.exe*
O que eles fazem é abrir o arquivo *DIMduct.py* usando o *python.exe* da pasta *python/*. Foi compilado usando **g++** com as flags **-mwindows**, **-static** e **-static-libgcc** (mais **-o DIMduct.exe** pro nome do arquivo final).
