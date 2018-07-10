# Versão utilizável

Nele é possível realizar todos os cálculos, retornando os mesmos resultados que o antigo DIMduct.
Porém, necessita ser interpretado/compilado por estar em *.py*. (necessário Python 3)

## Pasta *build-win-32/*

No diretório *build-win-32/* está presente o projeto em C++ do aplicativo, cujo foi gerado através do arquivo *projeto3.pdy* e a ferramenta **pyqtdeploy**. O próximo passo seria executar nesta pasta **qmake** (uma ferramenta do Qt) e, depois, **nmake** (um *.exe* presente nos arquivos dos Visual Studios; específico pra Windows), e então eu obteria um executável como desejado.
