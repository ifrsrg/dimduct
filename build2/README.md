# Segunda versão usável do DIMduct 2018.
Provavelmente melhor que a anterior, mas ainda é bem pesado e demora pra iniciar a primeira vez. Também o manual não está totalmente de acordo.

Pasta *python/* está compactada pra poder fazer upload, se for usar tem que descompactar.

## Sobre os *DIMduct.cpp* e *DIMduct.exe*
O que eles fazem é abrir o arquivo *DIMduct.py* usando o *python.exe* da pasta *python/*. Foi compilado usando **g++** atráves dos seguintes comandos (Windows cmd):

**g++ -Wall -c -g DIMduct.cpp -o DIMduct.o**

**g++ -static -static-libgcc -mwindows -static-libstdc++ -o DIMduct.exe DIMduct.o**
