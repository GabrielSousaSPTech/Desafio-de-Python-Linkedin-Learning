import secrets


class geradorSenhas():
    def gerarSenha(self, numeroPalavras):
        caminhoArquivo = 'C:\\diceware\\diceware.wordlist.pt.txt'
        with open(caminhoArquivo,'r', encoding='utf-8') as arquivo:
            linhaArquivo = arquivo.readlines()[3:7779]
            linha_separada = [line.split()[1] for line in linhaArquivo]
            codigoPalavra = [secrets.choice(linha_separada) for i in range(numeroPalavras)]
            return ' '.join(codigoPalavra)

    def descriptografarSenha(self, senha):
        caminhoArquivo = 'C:\\diceware\\diceware.wordlist.pt.txt'
        numeros = []

        with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
            linhaArquivo = arquivo.readlines()[3:7779]


            linha_separada = [line.strip().split() for line in linhaArquivo]



            for palavra in senha.split():
                for index, line in enumerate(linha_separada):
                    if palavra == line[1]:
                        if index > 0:
                            numero = linha_separada[index][0]
                            numeros.append(numero)
                        break

        return ' '.join(numeros), senha

g = geradorSenhas();

print(g.descriptografarSenha(g.gerarSenha(5)))

