from pathlib import Path
from collections import Counter
class ContandoPalavra:
    def contar(self, arquivo):

        conteudoArquivo = ''
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            conteudoArquivo = arquivo.read()
        palavra = conteudoArquivo.split(' ')
        contador = Counter(palavra);
        ranking = contador.most_common(20)
        for palavra, contagem in ranking:

            print(f'{palavra}: {contagem}')
        print(f'Numero total de palavras: { sum(contador.values())}')


c = ContandoPalavra()

c.contar('arquivos\\textoTeste.txt')
