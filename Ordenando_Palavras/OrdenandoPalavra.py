class OrdenarPalavra():
    def ordemAlfabetica(self, palavras):
        listaPalavra = palavras.split(" ")
        
        listaPalavra.sort(key=str.lower)

        return' '.join(listaPalavra)

o = OrdenarPalavra()

print(o.ordemAlfabetica("Maçã Banana LARANJA"))