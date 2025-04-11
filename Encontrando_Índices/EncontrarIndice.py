class EncontrarIndice():
    def localizarIndice(self, lista, indiceAencontrar):
        listaIndices = []
        for i, value in enumerate(lista):
            if indiceAencontrar == value:
                listaIndices.append([i])
            elif isinstance(lista[i], list):
                for j in self.localizarIndice(lista[i], indiceAencontrar):
                        listaIndices.append([i] + j)
        return listaIndices
    

e = EncontrarIndice()

print(e.localizarIndice([[[1,2,3],2,[1,3]],[1,2,3]], 2))

[[0,0,1],[0,1],[1,1]]